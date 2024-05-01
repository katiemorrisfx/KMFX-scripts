import fx
from PySide2 import QtWidgets
from PySide2 import QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import QLabel
import sys
from fx import *
from tools.objectIterator import getObjects
from tools.objectIterator import ObjectFinder



def callMethod(func, *args, **kwargs):
    def _return_func():
        return func(*args, **kwargs)
    return _return_func

# 
# START kmfx_alphaOverlayColor
# 

fx.prefs.add("KMFX.Alpha Overlay Color UI", True, hidden=True)

class KMFXalphaOverlayColor(Action):
    """allows to change the alpha overlay color with UI item and shortcuts"""

    def __init__(self,):
        Action.__init__(self, "KMFX|Alpha Overlay Color")
        # if fx.prefs["KMFX.Alpha Overlay Color UI"]:
        if not self.existingAObtn():

            self.AObtn = self.get_widgets()

            AOcolor = self.fxcolor_to_qcolor(fx.prefs["viewer.alphaColor"])
            self.AObtn.setStyleSheet(
                "background-color: {}".format(AOcolor.name()))

    def available(self):
        pass

    def execute(self, **kwargs):

        if "color" in kwargs.keys():
            fx.prefs["viewer.alphaColor"] = Color(
                kwargs["color"][0], kwargs["color"][1], kwargs["color"][2], fx.prefs["viewer.alphaColor"].a)
            AOcolor = self.fxcolor_to_qcolor(fx.prefs["viewer.alphaColor"])
            self.AObtn.setStyleSheet(
                "background-color: {}".format(AOcolor.name()))
        else:
            self.updateColor()

    def updateColor(self):
        # print(self.AObtn)
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.AObtn.setStyleSheet(
                "background-color: {}".format(color.name()))
            fx.prefs["viewer.alphaColor"] = self.qcolor_to_fxcolor(
                color, fx.prefs["viewer.alphaColor"])

    def fxcolor_to_qcolor(self, color):
        c = QtGui.QColor()
        c.setRgbF(color.r, color.g, color.b, color.a)
        return c

    def qcolor_to_fxcolor(self, qcolor, alpha):
        r = float(qcolor.red()/255.0)
        g = float(qcolor.green()/255.0)
        b = float(qcolor.blue()/255.0)
        return fx.Color(r, g, b, alpha.a)


    def existingAObtn(self):
        """Checks if the AO button already exists to avoid adding 
        multiple instances 
        
        Returns:
            TYPE: Boolean
        """
        widgets = QtWidgets.QApplication.allWidgets()
        plist = []

        AOfound = False
        for w in widgets:
            if AOfound:
                break
            try:
                if isinstance(w.parent().layout(),QtWidgets.QHBoxLayout):
                    if w.parent().layout().count() > 10 and w.parent() not in plist:
                        plist.append(w.parent())
                        for n in range(0, w.parent().layout().count()):
                            try:
                                x = w.parent().layout().itemAt(n).widget().text()
                                if x == "AO":
                                    AOfound = True
                                    break
                            except Exception:
                                pass
            except Exception:
                pass
        return AOfound


    def get_widgets(self):
        widgets = QtWidgets.QApplication.allWidgets()
        plist = []
        gammafound = False
        for w in widgets:
            if gammafound:
                break
            try:

                # to find the correct place (viewer), look for the Gamma label and a QLayout with lots 10+ items
                # found out that the layout that holds the target buttons is QHBoxLayout
                # so by filtering it the "count? WARNING" messages are avoided
                if isinstance(w.parent().layout(),QtWidgets.QHBoxLayout):
                    if w.parent().layout().count() > 10 and w.parent() not in plist:
                        plist.append(w.parent())
                        for n in range(0, w.parent().layout().count()):
                            try:
                                x = w.parent().layout().itemAt(n).widget().text()
                                if x == "Gamma":
                                    btn = QtWidgets.QPushButton("AO")
                                    if fx.prefs["KMFX.Alpha Overlay Color UI"]:
                                        w.parent().layout().addWidget(btn)
                                    btn.clicked.connect(self.updateColor)
                                    gammafound = True
                                    break

                            except Exception:
                                pass

            except Exception:
                pass

        return btn



# 
# END kmfx_alphaOverlayColor
# 
# 
# START kmfx_changepaintOpacity
# 


class KMFXchangepaintOpacity(Action):

    """shortcuts to increase/decrease opacity when using paint node"""

    def __init__(self):
        Action.__init__(self, "KMFX|Change Paint Opacity")

    def available(self):
        node = fx.activeNode()
        try:
            assert node.isType(
                "PaintNode") and node is not None, "Paint node not active"
        except Exception:
            pass

    def execute(self, **kwargs):
        beginUndo("KMFX|Change Paint Opacity")
        node = fx.activeNode()
        mode = kwargs["mode"] if "mode" in kwargs.keys() else "increase"
        if node.isType("PaintNode"):

            increment = 10 if mode == "increase" else -10
            x = fx.paint.opacity
            i = (x + increment) / 100
            fx.paint.opacity = i
        else:
            # this is only needed because the bind is made on keys 1 and 2
            fx.viewer.viewMode = 0 if mode == "increase" else 1
        endUndo()

# 
# END kmfx_changepaintOpacity
# 
# 
# START kmfx_cloneShapeinPlace
# 

def remove_keys(shape,propertiesList):
    for prop in propertiesList:
        propertie = shape.property(prop)
        editor = PropertyEditor(propertie)
        nkeys = propertie.numKeys
        if nkeys > 0:
            for t in reversed(range(nkeys)):
                editor.deleteKey(t)
        editor.execute()
        propertie.constant = True


class KMFXcloneShapeinPlace(Action):
    """Copy shapes to an Active Layer on a given frame,removing all keyframes."""

    def __init__(self):
        Action.__init__(self, "KMFX|Clone Shapes in Place")

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self,deletekeys=True,propertiesList=["opacity"]):
        beginUndo("KMFX Clone Shapes in Place") 
        shapes = getObjects(selection(), types=[Shape])
        activelayer = activeLayer()
        
        if activelayer != None: 
            thisframe_matrix = activelayer.getTransform(player.frame)
        else: ##shape is on the root of the node
            thisframe_matrix = Matrix()
            activelayer = activeNode()

        selectionlist = []
        avoid_duplicates = []
        for shape in shapes:
            # if shape.parent != activelayer and shape not in avoid_duplicates:
            if shape not in avoid_duplicates:
                copy = shape.clone()
                activelayer.property("objects").addObjects([copy])
                pathProp = copy.property("path")
                pathEditor = PropertyEditor(pathProp)
                path = copy.evalPath(player.frame)
                if shape.parent.type == "Layer":
                    identity = Matrix()
                    reverseparent = shape.parent.getTransform(player.frame)
                    offset_matrix = -thisframe_matrix  * reverseparent 
                    path.transform(offset_matrix)
                elif shape.parent.type == "RotoNode":
                    identity = Matrix()
                    reverseparent = identity
                    offset_matrix = -thisframe_matrix  * reverseparent 
                    path.transform(offset_matrix)
                    
                
                pathEditor.setValue(path, player.frame)
                keysn = pathProp.numKeys
                keys = pathProp.keys
                for t in reversed(range(keysn)):
                    if keys[t] != player.frame:
                        pathEditor.deleteKey(t)
                pathEditor.execute()
                
                if deletekeys:
                    remove_keys(copy,propertiesList)
                
                selectionlist.append(copy)
                avoid_duplicates.append(shape)
        select(selectionlist)
        endUndo()

# 
# END kmfx_cloneShapeinPlace
# 

# 
# START kmfx_copyShapeKeyframe
# 

class KMFXcopyShapeKeyframe(Action):
    """copy paste path keyframes"""

    def __init__(self):
        Action.__init__(self, "KMFX|Shape Keyframe Copy")
        self.savedkeys = {}
        self.from_action_menu = "copy"

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        shapes = getObjects(selection(), types=[Shape])

        if len(shapes) > 0:
            optype = kwargs["mode"] if "mode" in kwargs.keys() else self.from_action_menu

            if optype == "copy":
                self.savedkeys = {} ## start with fresh dict

            beginUndo("KMFX Shape Keyframe Paste")
            actualframe = player.frame

            for shape in shapes:
                path = shape.property("path")
                if optype=="copy":
                    self.savedkeys[shape.id] = path.getValue(actualframe)
                elif optype=="paste":
                    if shape.id in self.savedkeys.keys():
                        path.setValue(self.savedkeys[shape.id], actualframe)


            if optype == "paste":
                status("KMFX: pasted select shapes keyframes")
            else:
                status("KMFX: copied select shapes keyframes")       

            #alternating the actions if run from action menu
            # self.from_action_menu = "paste" if self.from_action_menu == "copy" else "copy"
            endUndo()
        else:
            status("KMFX: no shapes selected")




# 
# END kmfx_copyShapeKeyframe
# 
# 
# START kmfx_pasteShapeKeyframe
# 

class KMFXpasteShapeKeyframe(Action):
    """paste path keyframes, this is just a wrapper so we have this on the Actions menu"""

    def __init__(self):
        Action.__init__(self, "KMFX|Shape Keyframe Paste")

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        shapes = getObjects(selection(), types=[Shape])

        if len(shapes) > 0:
            fx.actions["KMFXcopyShapeKeyframe"].execute(**{"mode": "paste"})

        else:
            status("KMFX: no shapes selected")


# 
# END kmfx_pasteShapeKeyframe
# 
# 
# START kmfx_nudgeShapes
# 

class KMFXnudgeShapes(Action):
    """move shapes with keyboard shortcuts """

    def __init__(self,):
        Action.__init__(self, "KMFX|Nudge Shape Shortcuts")

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        beginUndo("KMFX move shape")
        node = activeNode()
        session = node.session
        session_size = session.size
        shapes = getObjects(selection(), types=[Shape])

        optype = kwargs["mode"] if "mode" in kwargs.keys() else "TL"

        multiplier = kwargs["modifier"] if "modifier" in kwargs.keys(
        ) else fx.prefs["nudging.distance"]

        if multiplier == "shift":
            multiplier = fx.prefs["nudging.extendedDistance"]
        elif multiplier == "ctrl":
            multiplier = fx.prefs["nudging.ctrlDistance"]

        mx = {"L": -1, "T": 0, "R": 1, "B": 0,
              "BL": -1, "TL": -1, "TR": 1, "BR": 1}
        my = {"L": 0, "T": -1, "R": 0, "B": 1,
              "BL": 1, "TL": -1, "TR": -1, "BR": 1}

        actualframe = player.frame
        for shape in shapes:
            selectedpoints = False if fx.viewer.toolName != "Reshape" else True
            pathProp = shape.property("path")
            pathEditor = PropertyEditor(pathProp)
            path = shape.evalPath(actualframe)
            matrix = Matrix()
            matrix.translate(1/session.size[0]/fx.viewer.zoom*mx[optype]*multiplier,
                             1/session.size[1]/fx.viewer.zoom*my[optype]*multiplier)
            path.transform(matrix, selected=selectedpoints)
            pathEditor.setValue(path, actualframe)
            pathEditor.execute()

        endUndo()

# 
# END kmfx_nudgeShapes
# 

# 
# START kmfx_resetcloneoverride
# 
fx.prefs.add("KMFX.Reset Clone also resets opacity", True,hidden=True)

class KMFXresetCloneOverride(Action):
    """replicates the behavior the clone tool
    "reset button",resets clone frame as well"""

    def __init__(self,):
        Action.__init__(self, "KMFX|Clone Reset transforms and frame")

    def available(self):
        assert fx.viewer.toolName == "Clone", "Clone tool only"

    def execute(self):
        beginUndo("KMFX Clone Reset transforms and frame")

        node = activeNode()

        if node.type == "PaintNode":
            fx.activeProject().save()  # small hack to force state to update

            clonelist = ["0", "1"]  # both clone presets

            for n in clonelist:
                if fx.prefs["KMFX.Reset Clone also resets opacity"] is True:
                    fx.paint.setState('opacity', 100)
                if node.state['paint']['Clone.frameRelative:'+n] is True:
                    fx.paint.setState('Clone.frame:'+n, 0)

                else:
                    fx.paint.setState('Clone.frame:'+n, player.frame)

                fx.paint.setState('Clone.position:'+n, Point3D(0, 0))
                fx.paint.setState('Clone.rotate:'+n, 0)
                fx.paint.setState('Clone.scale:'+n, Point3D(1, 1))

            fx.activeProject().save()

        endUndo()


# 
# END kmfx_resetcloneoverride
# 
# 
# START kmfx_selectallpoints
# 


# 
# START kmfx_timeOffset
# 

class KMFXtimeOffset(Action):
    """Offsets keyframes on selected nodes"""

    def __init__(self,):
        Action.__init__(self, "KMFX|Node Time Offset")

    def available(self):
        assert fx.selection() != [], "Select some nodes"

    def execute(self):
        if fx.selection() == []:
            displayError(
                "KMFXNode Time Offset: Select some nodes", title="Error")
            return

        num = {"id": "num", "label": "Frames to offset", "value": 0}
        direction = {"id": "list", "label": "Direction",
                     "value": "Head", "items": ["Head", "Tail"]}

        fields = [num, direction]
        result = getInput(title="Offset Node Keyframes", fields=fields)

        if result is not None:
            fx.beginUndo("KMFX Node time offset")

            offset = result['num'] * - \
                1 if result["list"] == "Head" else result['num']

            nodes = fx.selection()
            for node in nodes:
                if node.isType("PaintNode"):
                    pass  # cant change paint nodes at this time

                elif node.type in ["RotoNode", "MorphNode"]:
                    child = node.children
                    objects = getObjects(child)
                    selectedlist = []  # selection is just to refresh timeline

                    for o in objects:
                        if o.selected is True:
                            selectedlist.append(o)

                        for p in o.properties:
                            if o.property(p).constant is not True:
                                o.property(p).moveKeys(offset)

                # this is for all nodes properties

                for p in node.properties:
                    if node.property(p).constant is not True:
                        node.property(p).moveKeys(offset)
                x = fx.selection()
                fx.select([])
                fx.select(x)

            fx.endUndo()


# 
# END kmfx_timeOffset
# 


# 
# start kmfx_keyframeVisibility
# 


class KMFXkeyframeVisibility(Action):
    """Creates keyframes without clicking on the visibility icon"""

    def __init__(self):
        Action.__init__(self, "KMFX|Keyframe Visibility")

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        shapes = getObjects(selection(), types=[Shape])
        optype = kwargs["mode"] if "mode" in kwargs.keys() else "default"

        beginUndo("Keyframe Visibility ON/OFF")
        node = activeNode()
        session = node.session
        startFrame = session.startFrame

        actualframe = player.frame
        wasConstant = False
        for shape in shapes:
            opacity = shape.property("opacity")
            if opacity.constant:
                opacity.constant = False
                wasConstant = True

            if optype == "default":
                if opacity.getValue(actualframe) > 0:
                    opacity.setValue(0, actualframe)
                else:
                    opacity.setValue(100, actualframe)
                if wasConstant and actualframe != 0:
                    editor = PropertyEditor(opacity)
                    editor.deleteKey(0)
                    editor.execute()

            if optype == "singleframe":
                if actualframe not in (0, session.duration):
                    if opacity.getValue(actualframe) > 0:
                        opacity.setValue(0, actualframe-1)
                        opacity.setValue(100, actualframe)
                        opacity.setValue(0, actualframe+1)
                        if actualframe != 1 and wasConstant:
                            editor = PropertyEditor(opacity)
                            editor.deleteKey(0)
                            editor.execute()
                elif actualframe == 0:
                    if opacity.getValue(actualframe) > 0:
                        opacity.setValue(100, actualframe)
                        opacity.setValue(0, actualframe+1)
                elif actualframe == session.duration:
                    if opacity.getValue(actualframe) > 0:
                        opacity.setValue(0, actualframe-1)
                        opacity.setValue(100, actualframe)
                        editor = PropertyEditor(opacity)
                        editor.deleteKey(0)
                        editor.execute()

        endUndo()

# 
# end kmfx_keyframeVisibility
# 
#
# start KMFXmultikeyAssign
#
class KMFXmultikeyAssign(Action):
    """assign multiple actions to the same key shortcut depending on the active node context
    
    example:

    fx.bind('Num+1', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "decrease"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "BL"}] 
            }))


    the keys of the assignment dict should be: fx.activeNode().type i.e. PaintNode, RotoNode, etc
    the lists are [nameoftheaction (str), arguments (dict)]
    """

    def __init__(self,):
        Action.__init__(self, "KMFX|MultiKeyAssign helper")

    def available(self):
        pass
        
    def execute(self, **kwargs):
        node = activeNode()
        if node.type in kwargs.keys():
            print(kwargs)
            fx.actions[kwargs[node.type][0]].execute(**kwargs[node.type][1])






# 
# end KMFXmultikeyAssign
# 

#########################################
# the try/except on the actions is to prevent adding items to menu
# if you run megascript multiple times on console

try:
    action("KMFXmultikeyAssign")
except:
    addAction(KMFXmultikeyAssign())

#########################################
try:
    action("KMFXkeyframeVisibility")
except:   
    addAction(KMFXkeyframeVisibility())
fx.bind("Alt+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute, **{"mode": "default"}))
fx.bind("Alt+Shift+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute, **{"mode": "singleframe"}))
#########################################
try:
    action("KMFXtimeOffset")
except:   
    addAction(KMFXtimeOffset())
#########################################
try:
    action("KMFXresetCloneOverride")
except:
    addAction(KMFXresetCloneOverride())
fx.bind("Num+0", callMethod(fx.actions["KMFXresetCloneOverride"].execute))
#########################################
try:
    action("KMFXnudgeShapes")
except:
    addAction(KMFXnudgeShapes())

try:
    action("KMFXchangepaintOpacity")
except:   
    addAction(KMFXchangepaintOpacity())

fx.bind('Num+1', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "decrease"}],"RotoNode":["KMFXnudgeShapes", {"mode": "BL"}] 
            }))

fx.bind('Num+2', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "increase"}],"RotoNode":["KMFXnudgeShapes", {"mode": "B"}] 
            }))

fx.bind("6", callMethod(fx.actions["KMFXtimeOffset"].execute))

fx.bind("Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR"}))
fx.bind("Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL"}))
fx.bind("Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR"}))
fx.bind("Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T"}))
fx.bind("Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R"}))
fx.bind("Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L"}))

fx.bind("Shift+Num+1", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BL", "modifier": "shift"}))
fx.bind("Shift+Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR", "modifier": "shift"}))
fx.bind("Shift+Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL", "modifier": "shift"}))
fx.bind("Shift+Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR", "modifier": "shift"}))
fx.bind("Shift+Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T", "modifier": "shift"}))
fx.bind("Shift+Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R", "modifier": "shift"}))
fx.bind("Shift+Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L", "modifier": "shift"}))
fx.bind("Shift+Num+2", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "B", "modifier": "shift"}))

fx.bind("Ctrl+Num+1", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BL", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L", "modifier": "ctrl"}))
fx.bind("Ctrl+Num+2", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "B", "modifier": "ctrl"}))
#########################################
try:
    action("KMFXcopyShapeKeyframe")
except:
    addAction(KMFXcopyShapeKeyframe())
try:
    action("KMFXpasteShapeKeyframe")
except:
    addAction(KMFXpasteShapeKeyframe())
fx.bind("Ctrl+Shift+c", callMethod(fx.actions["KMFXcopyShapeKeyframe"].execute,**{"mode": "copy"})) 
fx.bind("Ctrl+Shift+v", callMethod(fx.actions["KMFXpasteShapeKeyframe"].execute,**{"mode": "paste"})) 
#########################################
try:
    action("KMFXcloneShapeinPlace")
except:
    addAction(KMFXcloneShapeinPlace())
fx.bind("Ctrl+Shift+d", callMethod(fx.actions["KMFXcloneShapeinPlace"].execute)) 
#########################################
try:
    action("KMFXalphaOverlayColor")
except:
    addAction(KMFXalphaOverlayColor())
fx.bind("Ctrl+9", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (0, 0, 0)})) #rgb values for black 0-1 range
fx.bind("Ctrl+0", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (1, 1, 1)})) #rgb values for white 0-1 range
#########################################

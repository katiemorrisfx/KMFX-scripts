import fx
from fx import *
from tools.objectIterator import getObjects
from tools.objectIterator import ObjectFinder

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
        node = activeNode()
        session = activeSession()
        assert session, "Select a Session"
        rotoNode = session.node(type="RotoNode")
        assert rotoNode, "The session does not contain a Roto Node"
        activelayer = activeLayer()
        assert activelayer != None, "Activate the destinationn Layer"
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


addAction(KMFXcloneShapeinPlace())

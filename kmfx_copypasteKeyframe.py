import fx
from fx import *
from tools.objectIterator import getObjects


class KMFXcopypasteKeyframe(Action):
    """copy paste path keyframes"""

    def __init__(self):
        Action.__init__(self, "KMFX|Copy Paste Shapes Keyframes")
        self.savedkeys = {}
        self.from_action_menu = "copy"


    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        shapes = getObjects(selection(), types=[Shape])

        if len(shapes) > 0:
            optype = kwargs["mode"] if "mode" in kwargs.keys() else self.from_action_menu

            beginUndo("KMFX Copy Paste Shape Keyframe")
            actualframe = player.frame

            if optype == "copy":
                self.savedkeys = {} ## start with fresh dict


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
            self.from_action_menu = "paste" if self.from_action_menu == "copy" else "copy"
            endUndo()
        else:
            status("KMFX: no shapes selected")


addAction(KMFXcopypasteKeyframe())

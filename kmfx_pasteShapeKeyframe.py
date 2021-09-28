import fx
from fx import *
from tools.objectIterator import getObjects
fx.prefs.add("KMFX_Load.Shape Keyframe Paste", True)


class KMFXpasteShapeKeyframe(Action):
    """paste path keyframes, this is just a wrapper so we have this on the Actions menu"""

    def __init__(self):
        if fx.prefs["KMFX_Load.Shape Keyframe Paste"] is True:
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


addAction(KMFXpasteShapeKeyframe())

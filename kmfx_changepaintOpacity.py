import fx
from fx import *


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


addAction(KMFXchangepaintOpacity())

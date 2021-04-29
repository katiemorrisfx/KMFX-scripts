import fx
from fx import *
from tools.objectIterator import getObjects


class KMFXselectAllPointRebind(Action):
    """shortcut to Selects all points when in reshape mode """

    def __init__(self,):
        Action.__init__(self, "KMFX|Select All Points rebind")

    def available(self):
        pass

    def execute(self):
        beginUndo("Select All Points rebind")
        if fx.viewer.toolName == "Reshape":
            fx.viewer.toolCommand("selectAllPoints")
        endUndo()


addAction(KMFXselectAllPointRebind())

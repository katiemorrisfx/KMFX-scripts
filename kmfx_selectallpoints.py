import fx
from fx import *
from tools.objectIterator import getObjects
fx.prefs.add("KMFX_Load.Select All Points rebind", True)


class KMFXselectAllPointRebind(Action):
    """shortcut to Selects all points when in reshape mode """

    def __init__(self,):
        if fx.prefs["KMFX_Load.Select All Points rebind"] is True:
            Action.__init__(self, "KMFX|Select All Points rebind")

    def available(self):
        pass

    def execute(self):
        beginUndo("Select All Points rebind")
        if fx.viewer.toolName == "Reshape":
            fx.viewer.toolCommand("selectAllPoints")
        endUndo()


addAction(KMFXselectAllPointRebind())

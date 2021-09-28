import fx
from fx import *
reshapeOverridestore = True
fx.prefs.add("KMFX_Load.Reshape Tool Override", True)

class KMFXreshapeOverride(Action):
    """Overrides the reshape tool binding to avoid the magnet reshape tool"""

    def __init__(self,):
        if fx.prefs["KMFX_Load.Reshape Tool Override"] is True:
            Action.__init__(self, "KMFX|Reshape Tool Override")

    def available(self):
        pass

    def execute(self):
        global reshapeOverridestore
        if reshapeOverridestore is True and fx.viewer.toolName != "Reshape":
            fx.viewer.selectTool("Reshape")
            reshapeOverridestore = False
        elif reshapeOverridestore is False and fx.viewer.toolName != "Reshape":
            fx.viewer.selectTool("Reshape")
            fx.viewer.selectTool("Transform")
            fx.viewer.selectTool("Reshape")


addAction(KMFXreshapeOverride())

import fx
from fx import *
clonemode = None
fx.prefs.add("KMFX_Load.Clone Interactive Toggle", True)


class KMFXcloneinteractivemodeToggle(Action):
    """shortcut to enable interactive mode if onion skin is active"""

    def __init__(self,):
        if fx.prefs["KMFX_Load.Clone Interactive Toggle"] is True:
            Action.__init__(self, "KMFX|Clone Interactive Toggle On/Off")

    def available(self):
        assert fx.viewer.toolName == "Clone", "Clone tool only"

    def execute(self):
        beginUndo("Clone Interactive Toggle On/Off")
        global clonemode

        print(clonemode)

        if fx.paint.onionSkin:
            # prevents entering interactive mode if onion skin is disabled
            if clonemode is None:
                # fx.paint.setOnionSkin(True)
                fx.paint.setTransformMode(True)
                clonemode = True

            else:
                fx.paint.setTransformMode(False)
                # fx.paint.setOnionSkin(True)
                clonemode = None
        endUndo()


addAction(KMFXcloneinteractivemodeToggle())

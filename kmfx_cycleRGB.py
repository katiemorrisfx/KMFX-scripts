import fx
from fx import *
cycleRGB = None
previousRGB = None
fx.prefs.add("KMFX_Load.Cycle RGB channels", True)


class KMFXcycleRGBchannels(Action):
    """Overrides shortcuts to cycle rgb modes using a single key shortcut"""

    def __init__(self,):
        if fx.prefs["KMFX_Load.Cycle RGB channels"] is True:
            Action.__init__(self, "KMFX|Cycle RGB channels")

    def available(self):
        pass

    def execute(self):
        beginUndo("Cycle RGB channels")
        global cycleRGB

        if cycleRGB is None:
            cycleRGB = fx.Color(1, 0, 0, 0)
            fx.viewer.setChannelMask(cycleRGB)
        elif cycleRGB == fx.Color(1, 0, 0, 0):
            cycleRGB = fx.Color(0, 1, 0, 0)
            fx.viewer.setChannelMask(fx.Color(cycleRGB))
        elif cycleRGB == fx.Color(0, 1, 0, 0):
            cycleRGB = fx.Color(0, 0, 1, 0)
            fx.viewer.setChannelMask(fx.Color(cycleRGB))
        else:
            cycleRGB = None
            fx.viewer.setChannelMask(fx.Color(1, 1, 1, 0))
        endUndo()


addAction(KMFXcycleRGBchannels())

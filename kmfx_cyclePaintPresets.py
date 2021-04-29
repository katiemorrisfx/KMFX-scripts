import fx
import sys
from fx import *

fx.prefs.add("KMFX.Paint Presets maximum cycle", 4, min=2, max=10)


class KMFXcyclePaintPresets(Action):
    """You can cycle your paint presets with a keybind"""

    def __init__(self,):
        Action.__init__(self, "KMFX|Cycle Paint Presets")

    def available(self):
        node = fx.activeNode()
        assert node is not None and node.isType(
            "PaintNode"), "Paint node not active"

    def execute(self):

        fx.beginUndo("Cycle_Paint_Presets")

        direction = 1
        node = fx.activeNode()

        num_presets = fx.prefs["KMFX.Paint Presets maximum cycle"]

        if node.type == "PaintNode":

            current = fx.paint.preset
            if current < 0:
                return
            index = current
            nextp = True
            while nextp is True:
                index = index + direction
                # handle wraparound
                if index < 0:
                    index = num_presets - 1
                elif index >= num_presets:
                    index = 0

                # avoid infinite loop if only one preset
                if index == current:
                    break

                # check for a preset
                try:
                    preset = node.state["preset%d" % (index)]
                    fx.paint.preset = index
                    nextp = False
                except Exception:
                    # e = sys.exc_info()
                    # print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    pass

        fx.endUndo()


addAction(KMFXcyclePaintPresets())

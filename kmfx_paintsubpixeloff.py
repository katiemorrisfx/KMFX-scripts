import fx
from fx import *


fx.prefs.add("KMFX.Disable Clone subpixel", True)


def KMFXnodeSelected():
    try:
        node = activeNode()
        if node.type == "PaintNode" and fx.prefs["KMFX.Disable Clone subpixel"] is True:
            fx.paint.setState('Clone.subpixel:0', 'False')
            fx.paint.setState('Clone.subpixel:1', 'False')
            # print("paint clone subpixel disabled by script")
    except Exception:
        pass


fx.hooks["node_selected"] = KMFXnodeSelected

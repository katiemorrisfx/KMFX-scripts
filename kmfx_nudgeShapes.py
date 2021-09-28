import fx
from fx import *
from tools.objectIterator import getObjects
fx.prefs.add("KMFX_Load.Nudge Shape Shortcuts", True)


class KMFXnudgeShapes(Action):
    """move shapes with keyboard shortcuts """

    def __init__(self,):
        if fx.prefs["KMFX_Load.Nudge Shape Shortcuts"] is True:
            Action.__init__(self, "KMFX|Nudge Shape Shortcuts")

    def available(self):
        shapes = getObjects(selection(), types=[Shape])
        assert len(shapes) > 0, "There must be one or more selected shapes"

    def execute(self, **kwargs):
        beginUndo("KMFX move shape")
        node = activeNode()
        session = node.session
        session_size = session.size
        shapes = getObjects(selection(), types=[Shape])

        optype = kwargs["mode"] if "mode" in kwargs.keys() else "TL"

        multiplier = kwargs["modifier"] if "modifier" in kwargs.keys(
        ) else fx.prefs["nudging.distance"]

        if multiplier == "shift":
            multiplier = fx.prefs["nudging.extendedDistance"]
        elif multiplier == "ctrl":
            multiplier = fx.prefs["nudging.ctrlDistance"]

        mx = {"L": -1, "T": 0, "R": 1, "B": 0,
              "BL": -1, "TL": -1, "TR": 1, "BR": 1}
        my = {"L": 0, "T": -1, "R": 0, "B": 1,
              "BL": 1, "TL": -1, "TR": -1, "BR": 1}

        actualframe = player.frame
        for shape in shapes:
            selectedpoints = False if fx.viewer.toolName != "Reshape" else True
            pathProp = shape.property("path")
            pathEditor = PropertyEditor(pathProp)
            path = shape.evalPath(actualframe)
            matrix = Matrix()
            matrix.translate(1/session.size[0]/fx.viewer.zoom*mx[optype]*multiplier,
                             1/session.size[1]/fx.viewer.zoom*my[optype]*multiplier)
            path.transform(matrix, selected=selectedpoints)
            pathEditor.setValue(path, actualframe)
            pathEditor.execute()

        endUndo()


addAction(KMFXnudgeShapes())

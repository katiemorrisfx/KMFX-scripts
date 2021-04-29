import fx
from fx import *
from tools.objectIterator import getObjects


class KMFXtimeOffset(Action):
    """Offsets keyframes on selected nodes"""

    def __init__(self,):
        Action.__init__(self, "KMFX|Node Time Offset")

    def available(self):
        assert fx.selection() != [], "Select some nodes"

    def execute(self):
        if fx.selection() == []:
            displayError(
                "KMFXNode Time Offset: Select some nodes", title="Error")
            return

        num = {"id": "num", "label": "Frames to offset", "value": 0}
        direction = {"id": "list", "label": "Direction",
                     "value": "Head", "items": ["Head", "Tail"]}

        fields = [num, direction]
        result = getInput(title="Offset Node Keyframes", fields=fields)

        if result is not None:
            fx.beginUndo("KMFX Node time offset")

            offset = result['num'] * - \
                1 if result["list"] == "Head" else result['num']

            nodes = fx.selection()
            for node in nodes:
                if node.isType("PaintNode"):
                    pass  # cant change paint nodes at this time

                elif node.type in ["RotoNode", "MorphNode"]:
                    child = node.children
                    objects = getObjects(child)
                    selectedlist = []  # selection is just to refresh timeline

                    for o in objects:
                        if o.selected is True:
                            selectedlist.append(o)

                        for p in o.properties:
                            if o.property(p).constant is not True:
                                o.property(p).moveKeys(offset)

                # this is for all nodes properties

                for p in node.properties:
                    if node.property(p).constant is not True:
                        node.property(p).moveKeys(offset)
                x = fx.selection()
                fx.select([])
                fx.select(x)

            fx.endUndo()


addAction(KMFXtimeOffset())

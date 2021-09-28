import fx
from fx import *
fx.prefs.add("KMFX_Load.Paint Hard Alpha setup", True)


class KMFX_hard_Alpha(Action):
    """creates a combo of nodes to setup a hard alpha"""

    def __init__(self,):
        if fx.prefs["KMFX_Load.Paint Hard Alpha setup"] is True:
            Action.__init__(self, "KMFX|Paint Hard Alpha setup")

    def available(self):
        assert fx.selection() != [], "Select some nodes"

    def execute(self):
        fx.beginUndo("Paint Hard Alpha setup")
        basenode = fx.selection()
        pos = basenode[0].state["graph.pos"]

        creatednodes = []
        if len(basenode) == 1:
            base = basenode[0]
            n1 = Node("com.digitalfilmtools.ofx.silhouette.sfx_copy")

            creatednodes.append(n1)
            activeSession().addNode(n1)
            try:
                n1.port("source").connect(base.port("output"))
                n1.port("target").connect(base.port("output"))
            except Exception:
                pass
            n1.property("red").setValue("Alpha")
            n1.property("blue").setValue("Alpha")
            n1.property("green").setValue("Alpha")

            """ setting the state (pos) for fresh nodes should be done inside a
             fx.beginUndo, otherwise the node Tree won't update correctly. """
            n1.setState('graph.pos', fx.Point3D(pos.x+150, pos.y))

            nn1 = n1
            for n in range(0, 4):
                n2 = Node("com.digitalfilmtools.ofx.silhouette.colorCorrect")
                activeSession().addNode(n2)
                n2.port("input").connect(nn1.port("Output"))
                n2.property("gamma").setValue(100)
                creatednodes.append(n2)
                n2.setState('graph.pos', fx.Point3D(
                    pos.x+150, pos.y+(50*(n+1))))
                nn1 = n2

            n3 = Node("com.digitalfilmtools.ofx.silhouette.sfx_copy")
            activeSession().addNode(n3)
            n3.port("source").connect(n2.port("Output"))
            n3.port("target").connect(base.port("output"))
            n3.property("alpha").setValue("Red")
            n3.setState('graph.pos', fx.Point3D(pos.x+150, pos.y+(50*5)))
            creatednodes.append(n3)

        fx.endUndo()


addAction(KMFX_hard_Alpha())

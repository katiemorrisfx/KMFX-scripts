import fx
from fx import *
from tools.objectIterator import getObjects


class KMFXmultikeyAssign(Action):
    """assign multiple actions to the same key shortcut depending on the active node context
    
    example:

    fx.bind('Num+1', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "decrease"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "BL"}] 
            }))


    the keys of the assignment dict should be: fx.activeNode().type i.e. PaintNode, RotoNode, etc
    the lists are [nameoftheaction (str), arguments (dict)]
    """

    def __init__(self,):
        Action.__init__(self, "KMFX|MultiKeyAssign helper")

    def available(self):
        pass
        
    def execute(self, **kwargs):
        node = activeNode()
        if node.type in kwargs.keys():
            fx.actions[kwargs[node.type][0]].execute(**kwargs[node.type][1])

addAction(KMFXmultikeyAssign())

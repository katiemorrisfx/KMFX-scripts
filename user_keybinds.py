import fx


def callMethod(func, *args, **kwargs):
    """ Helper function which returns a function that calls
        a specified method of an object, passing in the argument list.
        Used to replace 'lambda', which is being phased out
    
    Args:
        func (TYPE): Function

    Returns:
        TYPE: function
    """
    def _return_func():
        return func(*args, **kwargs)
    return _return_func

#########################################
fx.prefs.add("KMFX.Disable KMFX Keybinds", False)

if fx.prefs["KMFX.Disable KMFX Keybinds"] is False:

    if fx.prefs["KMFX_Load.Reshape Tool Override"] is True:
        # start reshape override #
        fx.unbind("r")
        fx.viewer.setToolBind("Reshape", "")
        fx.bind("r", callMethod(fx.actions["KMFXreshapeOverride"].execute))
        # end reshape override #

    fx.bind("Alt+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute, **{"mode": "default"}))
    fx.bind("Alt+Shift+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute, **{"mode": "singleframe"}))

    fx.bind("6", callMethod(fx.actions["KMFXtimeOffset"].execute))

    fx.bind("Num+0", callMethod(fx.actions["KMFXresetCloneOverride"].execute))

    fx.bind('Num+1', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "decrease"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "BL"}] 
            }))

    fx.bind('Num+2', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "increase"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "B"}] 
            }))

    fx.bind("Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR"}))
    fx.bind("Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL"}))
    fx.bind("Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR"}))
    fx.bind("Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T"}))
    fx.bind("Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R"}))
    fx.bind("Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L"}))

    fx.bind("Shift+Num+1", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BL", "modifier": "shift"}))
    fx.bind("Shift+Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR", "modifier": "shift"}))
    fx.bind("Shift+Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL", "modifier": "shift"}))
    fx.bind("Shift+Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR", "modifier": "shift"}))
    fx.bind("Shift+Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T", "modifier": "shift"}))
    fx.bind("Shift+Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R", "modifier": "shift"}))
    fx.bind("Shift+Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L", "modifier": "shift"}))
    fx.bind("Shift+Num+2", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "B", "modifier": "shift"}))

    fx.bind("Ctrl+Num+1", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BL", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L", "modifier": "ctrl"}))
    fx.bind("Ctrl+Num+2", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "B", "modifier": "ctrl"}))

    fx.bind("Ctrl+9", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (0, 0, 0)})) #rgb values for black 0-1 range
    fx.bind("Ctrl+0", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (1, 1, 1)})) #rgb values for white 0-1 range

    fx.bind("Ctrl+Shift+c", callMethod(fx.actions["KMFXcopyShapeKeyframe"].execute,**{"mode": "copy"})) 
    fx.bind("Ctrl+Shift+v", callMethod(fx.actions["KMFXpasteShapeKeyframe"].execute,**{"mode": "paste"})) 
    fx.bind("Ctrl+Shift+d", callMethod(fx.actions["KMFXcloneShapeinPlace"].execute)) 
    

    print("KM user keybinds loaded")
else:
    print("KM user keybinds disabled - check preferences")

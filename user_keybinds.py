import fx

# Helper function which returns a function that calls
# a specified method of an object, passing in the argument list.
# Used to replace 'lambda', which is being phased out
def callMethod(func, *args, **kwargs):
    def _return_func():
        return func(*args, **kwargs)
    return _return_func

#########################################
print("KM user keybinds loaded")


#### start reshape override ####
fx.unbind("r")
fx.viewer.setToolBind("Reshape", "")
fx.bind("r", callMethod(fx.actions["KMFXreshapeOverride"].execute))
### end reshape override ####



fx.bind("Alt+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute,**{"mode":"default"}))
fx.bind("Alt+Shift+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute,**{"mode":"singleframe"}))

fx.bind("i", callMethod(fx.actions["KMFXcloneinteractivemodeToggle"].execute))


fx.bind("5", callMethod(fx.actions["KMFXcycleRGBchannels"].execute))
fx.bind("6", callMethod(fx.actions["KMFXtimeOffset"].execute))

fx.bind("Num+0", callMethod(fx.actions["KMFXresetCloneOverride"].execute))

fx.bind("Num+1", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"save"}))
fx.bind("Num+2", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"load"}))

fx.bind("v", callMethod(fx.actions["KMFXselectAllPointRebind"].execute))
fx.bind("TAB", callMethod(fx.actions["KMFXcyclePaintPresets"].execute))

fx.bind('1', callMethod(fx.actions["KMFXchangepaintOpacity"].execute,**{"mode":"decrease"}))
fx.bind('2', callMethod(fx.actions["KMFXchangepaintOpacity"].execute,**{"mode":"increase"}))






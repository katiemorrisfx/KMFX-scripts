## KMFX_reshapeOverride Documentation

This script allows you to override the toggling of the Reshape tool with the Magnetic tool (avoiding entering on the Magnetic).  
Magnetic mode will still be accessible, but you need to click with the mouse on the toolbar.

Steps:

1. When pressing the "r" key in the Roto node it will no longer toggle between the Magnetic tool and will remain in the
Reshape tool.


- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command

```
fx.unbind("r")
fx.viewer.setToolBind("Reshape", "")
fx.bind("r", callMethod(fx.actions["KMFXreshapeOverride"].execute))
```
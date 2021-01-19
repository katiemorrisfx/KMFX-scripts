## KMFX_selectallpoints Documentation

This script allows you to select all of the points on a shape with a single hotkey.

Steps:

1. To select all of the points on a shape, select the shape, then click "v"

Note: The default hotkey for this was "alt/option+shift+a" and is now rebound to "v"

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("v", callMethod(fx.actions["KMFXselectAllPointRebind"].execute))
```
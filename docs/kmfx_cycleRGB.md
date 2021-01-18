## KMFX_cycleRGB Documentation

This script allows you to change what channels the Silhouette Viewer displays
using a hotkey shortcut, cycling between R, G, B and RGB with each press of the hotkey,
"5".

Note: The default hotkey "5" binding overrides Silhouette's View Input 5 or View Composite
function, depending on the selected node.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("5", callMethod(fx.actions["KMFXcycleRGBchannels"].execute))
```
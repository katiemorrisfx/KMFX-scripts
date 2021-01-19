## KMFX_resetcloneoverride Documentation

This script allows you to reset the frame, transformations and opacity in the Paint tab.

Steps: 

1. Click the "0" on the numeric keypad to reset the frame number and any transformations.
2. Optional: One can check "Reset Clone also resets opacity" in KMFX Preferences if you also want the opacity to be reset to 100%

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("Num+0", callMethod(fx.actions["KMFXresetCloneOverride"].execute))
```
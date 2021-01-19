## KMFX_cyclePaintPresets Documentation

This script allows you cycle between your Paint Presets by using the "TAB" key.


Note: Set the Paint Presets Maximum cycle number in the KMFX Preferences to the number of presets you have. 
You can also just leave the cycle number to 10 and it will cycle through whatever number of presets you have.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("TAB", callMethod(fx.actions["KMFXcyclePaintPresets"].execute))
```
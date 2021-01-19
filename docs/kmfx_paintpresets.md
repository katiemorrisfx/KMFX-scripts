## KMFX_paintpresets Documentation

This script allows you save and load paint presets with the assigned keybinds.

Steps:
1. While in a Paint node, make and save any number of paint presets in the Presets tab in the Paint window.
2. Press "1" on the numeric keypad to save your presets and name it.
3. To load in saved presets, press "2" on the numeric keypad to bring up the gui that has the List of
possible presets that can be loaded in.

Note: Presets are saved in folders named with the saved preset name in the "paint_presets" folder inside of KMFX scripts. 
There is also an option to save a preset to a specified folder, inside of KMFX Preferences.


- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("Num+1", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"save"}))
fx.bind("Num+2", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"load"}))
```


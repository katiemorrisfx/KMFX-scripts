## KMFX_paintpresets Documentation

This script allows you save and load paint presets with the assigned keybinds.

Steps:
1. While in a Paint node, make and save any number of paint presets in the Presets tab in the Paint window.
2. From KMFX menu, select Paint Presets (or use the keybinds Alt+1 (save), Alt+2 (load) on the numeric keypad)

You *must* set up the "Paint Presets Path" folder in KMFX preferences to designate a place to save your presets.


## Preferences

(Silhouette > Preferences > KMFX)

There is also an option to save the preset to a specified folder, inside of KMFX Preferences.

You can share your presets with other users or move them to another computer, just copy the whole presets folder to the new location.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example

<a href="http://www.youtube.com/watch?feature=player_embedded&v=9xNt4gf3qeo" target="_blank"><img src="http://img.youtube.com/vi/9xNt4gf3qeo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>

<a href="http://www.youtube.com/watch?feature=player_embedded&v=LcLVUW5JeC4" target="_blank"><img src="http://img.youtube.com/vi/LcLVUW5JeC4/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("Alt+Num+1", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"save"}))
fx.bind("Alt+Num+2", callMethod(fx.actions["KMFXpaintPresets"].execute,**{"mode":"load"}))
```


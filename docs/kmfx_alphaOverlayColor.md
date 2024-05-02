## KMFX_keyframeVisibility Documentation

This script add a UI button to change the color of the alpha overlay.  When you click on it it brings up the color picker.  This is for Silhouette versions v 2022.5 and upwards.

You can use designated keybinds to cycle between two preset color for the alpha overlay.  The use can set up custiom hotkeys for R,G,B values. 
To enable the overlay either use the A keys to cycle, or use Shift+A.  
There is a checkbox in KMFX scripts preferences that lets users disable the button on the UI.  One has to restart after changing that box.
Currently, Ctrl/Cmd+9 (black) and Ctrl/Cmd+0 (white) are assigned keybinds.  These are set in the user_keybinds.py file.

- Can be run from KMFX menu:  YES
- Can be run from keybind:  YES





## Sample Keybind Command
```

fx.bind("Ctrl+9", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (0, 0, 0)})) #rgb values for black 0-1 range
fx.bind("Ctrl+0", callMethod(fx.actions["KMFXalphaOverlayColor"].execute, **{"color": (1, 1, 1)})) #rgb values for white 0-1 range
```

## KMFX_nudgeShapes Documentation

This script allows you to nudge Shapes and Shapes Points with the numeric keypad (up, down, left, right and diagonals)
Nudge modifiers are set up on regular Silhouette Preferences > Nudge

Steps:
1. Select shapes or shape points
2. Press "1" to "9"  on the numeric keypad move. Hold Shift or Ctrol for nudge modiers.<br>
"1","3","7","9" move diagonally.




## Preferences

- Can be run from KMFX menu: No
- Can be run from keybind: YES


## Video Example

<a href="http://www.youtube.com/watch?feature=player_embedded&v=HW4uZwjBp4s" target="_blank"><img src="http://img.youtube.com/vi/HW4uZwjBp4s/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("Num+1", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BL"}))
fx.bind("Num+3", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "BR"}))
fx.bind("Num+7", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TL"}))
fx.bind("Num+9", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "TR"}))
fx.bind("Num+8", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "T"}))
fx.bind("Num+6", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "R"}))
fx.bind("Num+4", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "L"}))
fx.bind("Num+2", callMethod(fx.actions["KMFXnudgeShapes"].execute, **{"mode": "B"}))

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
```


## KMFX_cloneshapeinPlace Documentation

This script allows one to copy shapes to an active layer on a given frame, removing all keyframes.  For Silhouette versions v2022.5 and upwards.

Steps/Notes:
1. A shape is selected, typically one that has keyframes, then click the hotkey shortcut (Cmd+Shift+D), make sure the layer that the shape is
currently in is unselected.  It does not matter if it is on a keyframe or not.
2. It creates a copy of the shape on the same position and makes a keyframe, but it won't be in the layer that 
it was originally in if that layer is unselected.
3. If no other layer is selected it will be copied to root.
4. If another layer is selected, then the shape will go into that layer
5. The result is a shape with a single keyframe.
6. Shapes and colors remain the same.
7. Multiple shapes can be done at the same time.

- Can be run from KMFX menu:  YES
- Can be frun from keybind:  YES



```

fx.bind("Ctrl+Shift+d", callMethod(fx.actions["KMFXcloneShapeinPlace"].execute)) 
```


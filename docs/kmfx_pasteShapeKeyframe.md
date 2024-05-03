## KMFX_pasteShapeKeyframe Documentation

This scripts lets the user paste a shape that has been previously copied with the copyShapeKeyframe script.  For Silhouette versions v2022.5 and upwards.

Use the currently assigned hotkey shortcut (Cmd+Shift+v) to paste a copied shape keyframe.  If multiple shapes have been copied, then multiple shapes will be pasted.

- Can be run from the KMFX menu:  YES
- Can be run from the keybind:  YES




## Sample Keybind Command
```

fx.bind("Ctrl+Shift+v", callMethod(fx.actions["KMFXpasteShapeKeyframe"].execute,**{"mode": "paste"}))
```

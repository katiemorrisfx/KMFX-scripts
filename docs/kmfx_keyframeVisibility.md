## KMFX_keyframeVisibility Documentation

This script allows you to change the visibility of a keyframe on a roto shape using a hotkey shortcut.  This is for Silhouette versions v2022.5 and upwards.

Steps:
1. Select the roto shape and use the hotkey to disable or enable opacity, you do not have to be on a shape
keyframe.  If not on a shape keyframe, a visibility keyframe will be made but a shape keyframe will not be made.
2. To have a shape on only for a single frame then use the hotkey shortcut with the modifier, as noted.  You do have to 
be on a shape keyframe for this to work.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example

<a href="http://www.youtube.com/watch?feature=player_embedded&v=iCOpkhIJKOs" target="_blank"><img src="http://img.youtube.com/vi/iCOpkhIJKOs/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("Alt+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute,**{"mode":"default"}))
fx.bind("Alt+Shift+o", callMethod(fx.actions["KMFXkeyframeVisibility"].execute,**{"mode":"singleframe"}))
```


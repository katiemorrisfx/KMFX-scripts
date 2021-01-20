## KMFX_timeOffset Documentation

This script allows you to offset keyframes if the length of your shot changes.  This works with the
Roto node, keyframeable attributes inside the Roto node, such as Blur, and other nodes that have keyframes with exception of the Paint node paint strokes.


Steps: One of two methods, and the example here is if 10 frames have been added to the head 
1. Load in new footage into your Silhouette Project
2. Make a new Session with the new footage, it will reflect the new startframe and new length
3. Copy the original roto node in the original Session and copy it into your new Session and attach it to your new footage
4. Select the node and press the hotkey on the keyboard or the numeric keypad, and a gui pops up
5. Change the "Frames to offset" amount to 10, and the "Direction" pulldown to Tail
6. Your keyframes will be moved to the correct location automatically

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("6", callMethod(fx.actions["KMFXtimeOffset"].execute))
```

Note: The default hotkey "6" binding overrides Silhouette's View Input 6 or View Channels
function, depending on the selected node.
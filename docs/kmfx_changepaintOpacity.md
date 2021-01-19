## KMFX_changepaintOpacity Documentation

This script allows you to increase or decrease the paint opacity using hotkeys.

The decrease keybind ('1' key on the example below) will reduce paint opacity by 10%, and the increase keybind ('2' below) key will increase the paint opacity
by 10%.

- Can be run from KMFX menu: NO
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind('1', callMethod(fx.actions["KMFXchangepaintOpacity"].execute,**{"mode":"decrease"})) 
fx.bind('2', callMethod(fx.actions["KMFXchangepaintOpacity"].execute,**{"mode":"increase"}))
```

Note: The default hotkeys "1" and "2" bindings override Silhouette's Output View "1" and Foreground View "2" hotkeys 
when in the Paint node.  The hotkeys work on the keyboard, not the numeric keypad. For numeric use "Num+1", "Num+2".

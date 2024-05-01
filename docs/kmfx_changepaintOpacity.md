## KMFX_changepaintOpacity Documentation

This script allows you to increase or decrease the paint opacity using hotkeys when in the Paint Node.  For Silhouette versions v2022.5 and upwards.

The decrease keybind ('Num+1' key on the example below) will reduce paint opacity by 10%, and the increase keybind ('Num+2' below) key will increase the paint opacity
by 10%.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example

<a href="http://www.youtube.com/watch?feature=player_embedded&v=-zJ9LGz4HjQ" target="_blank"><img src="http://img.youtube.com/vi/-zJ9LGz4HjQ/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind('Num+1', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "decrease"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "BL"}] 
            }))

    fx.bind('Num+2', callMethod(fx.actions["KMFXmultikeyAssign"].execute,
        **{"PaintNode":["KMFXchangepaintOpacity", {"mode": "increase"}],
            "RotoNode":["KMFXnudgeShapes", {"mode": "B"}] 
            }))
```

Note: The default hotkeys "Num+1" and "Num+2" bindings override Silhouette's Output View and Foreground View hotkeys 
when in the Paint node.  

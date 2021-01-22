## KMFX_cloneinteractivemodeToggle Documentation

This script allows you to turn off the Interactive on-screen controls with a hotkey, without having to press
the Interactive button in the Clone tab window.

Steps: 
1. Press Caps Lock to enter Onion Skin mode
2. Press assigned keybind to enter into the Onion Skin mode, enable Interactive mode and the Interactive on-screen controls
3. Make adjustments
4. Press assigned keybind to leave Interactive mode and disable the Interactive on-screen controls
5. Press Caps Lock to disable Onion Skin mode
6. Paint

Note: While using the assigned keybind, the Interactive button in the Clone tab window will not become highlighted.

- Can be run from KMFX menu: YES
- Can be run from keybind: YES


## Video Example
Coming soon

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aYSGDXyM6oo" target="_blank"><img src="http://img.youtube.com/vi/aYSGDXyM6oo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>


## Sample Keybind Command
```
fx.bind("i", callMethod(fx.actions["KMFXcloneinteractivemodeToggle"].execute))
```
# py-window-manipulation
This quick 'n' dirty script manipulates windows from other applications, using the python win32 libraries.

Use the "WindowManipulationManager" class (WMM) to manipulate windows from other applications.  

## Requirements

To use this library, the pywin32 package must be installed.
The pywin32 project can be found [here](https://github.com/mhammond/pywin32).
Binary releases can be downloaded from [here](https://github.com/mhammond/pywin32/releases).

## How to use

To use the library, you can check the [manipulateWindowExample.py](manipulateWindowExample.py) example.

The function ``` "find_window_wildcard(".*<SearchString>*")"``` registers the handle of the matching window. 
If there is a matching result, you can start to manipulate the window.

For example, there are following options:
- Edit the style of a window, with following options (resizable,sysmenu,maximizebox,minimizebox,                      closeable,border,titlebar,sizebox,taskbarIcon)
- Set a window to the foreground
- Set a window to fullscreen
- Find child windows in parent window
- Move window to given position
- Remove menu bar of a window (or child window)
- Get monitors info
- ...

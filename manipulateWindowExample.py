import WMM

w = WMM.WindowManipulationManager()

if w.find_window_wildcard(".*Micro Browser*"):
    if w.prepare_style_build():
        w.style_builder(resizable=False,sysmenu=False,minimizebox=False,maximizebox=False,closeable=False,border=False,titlebar=False,sizebox=False,taskbarIcon=True)
        w.set_defined_style()
    w.remove_menubar()
    w.set_foreground()
    w.set_FullScreen()

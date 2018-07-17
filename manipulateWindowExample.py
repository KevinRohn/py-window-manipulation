import sys, os
sys.path.append(os.getcwd()+ r"\modules")
import WMM

w = WMM.WindowManipulationManager()

if w.find_window_wildcard(".*Browser*"):
    if w.prepare_style_build():
        w.style_builder(resizable=False,sysmenu=False,minimizebox=False,maximizebox=False,closeable=False,border=False,titlebar=False,sizebox=False,taskbarIcon=True)
        w.set_defined_style()
    w.remove_menubar()
    w.set_foreground()
    try:
        monitorInfo1 = w.get_info_for_monitor(1)
        w.move_window_to_pos(monitorInfo1['Monitor'])
    except:
        print("no Monitor found")
    w.set_FullScreen()

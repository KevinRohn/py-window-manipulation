import sys, os
sys.path.append(os.getcwd()+ r"\modules")
import WMM
import time
import subprocess



w = WMM.WindowManipulationManager()

def startProgram(programm="", args=""):
    subprocess.Popen(programm+"" + args+ "")  

def renameWindow(title=""):
    w.set_window_title(title)

def findWindow():
    if w.find_window_wildcard(".*Micro*"):
        return True
        
def moveWindow(move=None,monitor=0):
    if w.prepare_style_build():
        w.style_builder(resizable=False,sysmenu=False,minimizebox=False,maximizebox=False,closeable=False,border=False,titlebar=False,sizebox=False,taskbarIcon=True)
        w.set_defined_style()
        w.remove_menubar()
        w.set_foreground()

    if move is not None:  
        if move:
            try:
                monitorInfo = w.get_info_for_monitor(monitor)
                w.move_window_to_pos(monitorInfo['Monitor'])
            except:
                print("no Monitor found")
    else:
        w.set_FullScreen()

startProgram("http://<IP>")
time.sleep(5)
if findWindow():
    renameWindow("New Title")
    time.sleep(5)
    moveWindow(move=True,monitor=0)
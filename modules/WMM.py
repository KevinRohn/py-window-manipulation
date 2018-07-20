import win32gui
import win32api
import win32con
import json
import re

class WindowManipulationManager(object):
### See Window Style documentation to get an overview https://docs.microsoft.com/en-us/windows/desktop/winmsg/window-styles

    # init
    def __init__ (self):       
        self._handle = None
        self._style = win32con.GWL_STYLE
        self._extStyle = win32con.GWL_EXSTYLE

    # find window by class name
    def find_window(self, ClassNname, WindowName=None):
        self._handle = win32gui.FindWindow(ClassNname, WindowName)

    # pass to ceck all the opened windows -- Parent Window --
    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    # find window with matched wildcard name -- Parent Window --
    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
        print(self._handle)
        if self._handle is not None:
            return True
        else:
            return False

    # return the handler
    def get_handle(self):
        return self._handle
    
    # set a window title
    def set_window_title(self,title=""):
        win32gui.SetWindowText(self._handle, title)

    # get all child windows
    def get_child_windows(self):
        if not self._handle:  
            return  
        child_window_list = []  
        win32gui.EnumChildWindows(self._handle, lambda hWnd, param: param.append(hWnd), child_window_list)  
        return child_window_list       

    # set style build
    def prepare_style_build(self):
        if self._handle is not None:
            self._style = win32api.GetWindowLong(self._handle, win32con.GWL_STYLE)
            self._extStyle = win32api.GetWindowLong(self._handle, win32con.GWL_EXSTYLE)
        if self._style and self._extStyle is not 0: 
            return True
        else:
            return False
    # set the window to the foreground
    def set_foreground(self):
        if not self._handle:  
            return  
        win32gui.SetForegroundWindow(self._handle)

    # set the window to fullscreen
    def set_FullScreen(self):
        if not self._handle:  
            return 
        win32gui.ShowWindow(self._handle, win32con.SW_MINIMIZE)
        win32gui.ShowWindow(self._handle, win32con.SW_MAXIMIZE)

    # Basic style builder
    def style_builder(self,resizable=None,sysmenu=None,maximizebox=None,minimizebox=None,
                      closeable=None,border=None,titlebar=None,sizebox=None,
                      taskbarIcon=None):
        if resizable is not None:
            if resizable:
                self._style &= win32con.WS_SIZEBOX
            else:
                self._style &= ~win32con.WS_SIZEBOX
        if sysmenu is not None:
            if sysmenu:
                self._style &= win32con.WS_SYSMENU
            else:
                self._style &= ~win32con.WS_SYSMENU
        if minimizebox is not None:
            if minimizebox:
                self._style &= win32con.WS_MINIMIZEBOX
            else:
                self._style &= ~win32con.WS_MINIMIZEBOX 
        if maximizebox is not None:
            if maximizebox:
                self._style &= win32con.WS_MAXIMIZEBOX
            else:
                self._style &= ~win32con.WS_MAXIMIZEBOX

        if border is not None:
            if border:
                self._style &= win32con.WS_BORDER
                #self._style &= win32con.WS_DLGFRAME 
                self._style &= win32con.WS_THICKFRAME
                self._style &= win32con.WS_EX_CLIENTEDGE
                self._style &= win32con.WS_EX_DLGMODALFRAME
                self._style &= win32con.WS_EX_WINDOWEDGE
            else: 
                self._style &= ~win32con.WS_BORDER
                #self._style &= ~win32con.WS_DLGFRAME
                self._style &= ~win32con.WS_THICKFRAME
                self._style &= ~win32con.WS_EX_CLIENTEDGE
                self._style &= ~win32con.WS_EX_DLGMODALFRAME
                self._style &= ~win32con.WS_EX_STATICEDGE
                self._style &= ~win32con.WS_EX_WINDOWEDGE

        if titlebar is not None:
            if titlebar:
                self._style &= win32con.WS_CAPTION
            else:
                self._style &= ~win32con.WS_CAPTION

        if sizebox is not None:
            if sizebox:
                self._style &= win32con.WS_SIZEBOX
            else:
                self._style &= ~win32con.WS_SIZEBOX

        if taskbarIcon is not None:
            if taskbarIcon:
                self._extStyle &= win32con.WS_EX_TOOLWINDOW
            else:
                self._extStyle &= ~win32con.WS_EX_TOOLWINDOW

    # get Monitor info
    def get_info_for_monitor(self, monitor_ID):
        mon = win32api.EnumDisplayMonitors()
        moninfo = None
        try:            
            moninfo = (win32api.GetMonitorInfo(mon[monitor_ID][0]))
            moninfodump = json.dumps(moninfo)
            moninfojsonload = json.loads(moninfodump)
        except: 
            print("Monitor ID seems to be like out of the index range")
        return moninfojsonload
    
    # move window to given position
    def move_window_to_pos(self, position):
        win32gui.MoveWindow(self._handle,position[0],position[1],position[2],position[3],True)
        win32gui.SetWindowPos

    # removes the windows menu bar
    def remove_menubar(self):
        win32gui.SetMenu(self._handle, None)
        

    # set the defined style
    def set_defined_style(self):
        win32gui.ShowWindow(self._handle, win32con.SW_HIDE)
        win32gui.SetWindowLong(self._handle,win32con.GWL_STYLE,self._style)
        win32gui.SetWindowLong(self._handle,win32con.GWL_EXSTYLE,self._extStyle)
        win32gui.ShowWindow(self._handle,win32con.SW_SHOW)


class WMMError(Exception):
    def __init__(self,value):
        self._value = value
    def __str__(self):
        return repr(self._value)
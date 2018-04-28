from pyplex.glfw import _glfw

import ctypes
from typing import Optional, Callable, List


# ..:: GLFW Structs ::.. #
class Window(ctypes.Structure):
    """GLFW Window Object"""

    _fields_ = [("id", ctypes.c_int)]


class Monitor(ctypes.Structure):
    """GLFW Monitor Object"""

    _fields_ = [("id", ctypes.c_int)]


class VideoMode(ctypes.Structure):
    """GLFW VideoMode Object"""

    _fields_ = [("width", ctypes.c_int),
                ("height", ctypes.c_int),
                ("red_bits", ctypes.c_int),
                ("green_bits", ctypes.c_int),
                ("blue_bits", ctypes.c_int),
                ("refresh_rate", ctypes.c_uint)]


# ..:: GLFW Functions ::.. #
_glfw.glfwInit.restype = ctypes.c_int
_glfw.glfwInit.argtypes = []
def init() -> int:
    return _glfw.glfwInit()


_glfw.glfwTerminate.restype = None
_glfw.glfwTerminate.argtypes = []
def terminate():
    return _glfw.glfwTerminate()


_glfw.glfwGetPrimaryMonitor.restype = ctypes.POINTER(Monitor)
_glfw.glfwGetPrimaryMonitor.argtypes = []
def get_primary_monitor():
    return _glfw.glfwGetPrimaryMonitor()


_glfw.glfwGetMonitors.restype = ctypes.POINTER(ctypes.POINTER(Monitor))
_glfw.glfwGetMonitors.argtypes = [ctypes.POINTER(ctypes.c_int)]
def get_monitors() -> List[Monitor]:
    count = ctypes.c_int(0)
    count_ptr = ctypes.pointer(count)
    monitors = _glfw.glfwGetMonitors(count_ptr)
    return [monitors[i] for i in range(count.value)]


_glfw.glfwGetMonitorPos.restype = None
_glfw.glfwGetMonitorPos.argtypes = [ctypes.POINTER(Monitor), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
def get_monitor_pos(monitor: Monitor):
    x, y = ctypes.c_int(0), ctypes.c_int(0)
    x_ptr, y_ptr = ctypes.pointer(x), ctypes.pointer(y)
    _glfw.glfwGetMinitorPos(monitor, x_ptr, y_ptr)
    return x.value, y.value


_glfw.glfwGetMonitorPhysicalSize.restype = None
_glfw.glfwGetMonitorPhysicalSize.argtypes = [ctypes.POINTER(Monitor),
                                             ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
def get_monitor_physical_size(monitor: Monitor):
    width, height = ctypes.c_int(0), ctypes.c_int(0)
    width_prt, height_ptr = ctypes.pointer(width), ctypes.pointer(height)
    _glfw.glfwGetMonitorPhysicalSize(monitor, width_prt, height_ptr)
    return width.value, height.value


_glfw.glfwGetMonitorName.restype = ctypes.c_char_p
_glfw.glfwGetMonitorName.argtypes = [ctypes.POINTER(Monitor)]
def get_monitor_name(monitor: Monitor) -> str:
    return _glfw.glfwGetMonitorName(monitor).decode()


_glfw.glfwGetVideoModes.restype = ctypes.POINTER(VideoMode)
_glfw.glfwGetVideoModes.argtypes = [ctypes.POINTER(Monitor), ctypes.POINTER(ctypes.c_int)]
def get_video_modes(monitor: Monitor) -> List[VideoMode]:
    count = ctypes.c_int(0)
    count_ptr = ctypes.pointer(count)
    video_modes = _glfw.glfwGetVideoModes(monitor, count_ptr)
    return [video_modes[i] for i in range(count.value)]


_glfw.glfwGetVideoMode.restype = ctypes.POINTER(VideoMode)
_glfw.glfwGetVideoMode.argtypes = [ctypes.POINTER(Monitor)]
def get_video_mode(monitor: Monitor) -> VideoMode:
    return _glfw.glfwGetVideoMode(monitor).contents


_glfw.glfwCreateWindow.restype = ctypes.POINTER(Window)
_glfw.glfwCreateWindow.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p,
                                   ctypes.POINTER(Monitor), ctypes.POINTER(Window)]
def create_window(width: int, height: int, title: str,
                  monitor: Optional[Monitor] = None, share: Optional[Window] = None) -> Window:
    return _glfw.glfwCreateWindow(width, height, title.encode(), monitor, share)


_glfw.glfwDestroyWindow.restype = None
_glfw.glfwDestroyWindow.argtypes = [ctypes.POINTER(Window)]
def destroy_window(window: Window):
    _glfw.glfwDestroyWindow(window)


_glfw.glfwWindowHint.restype = None
_glfw.glfwWindowHint.argtypes = [ctypes.c_int, ctypes.c_int]
def window_hint(target: int, value: int):
    _glfw.glfwWindowHint(target, value)


_glfw.glfwDefaultWindowHints.restype = None
_glfw.glfwDefaultWindowHints.argtypes = []
def default_window_hints():
    _glfw.glfwDefaultWindowHints()


_glfw.glfwSetWindowShouldClose.restype = None
_glfw.glfwSetWindowShouldClose.argtypes = [ctypes.POINTER(Window), ctypes.c_int]
def set_window_should_close(window: Window, value: bool):
    _glfw.glfwWindowShouldClose(window, value)


_glfw.glfwWindowShouldClose.restype = ctypes.c_int
_glfw.glfwWindowShouldClose.argtypes = [ctypes.POINTER(Window)]
def window_should_close(window: Window):
    return _glfw.glfwWindowShouldClose(window)


_glfw.glfwMakeContextCurrent.restype = None
_glfw.glfwMakeContextCurrent.argtypes = [ctypes.POINTER(Window)]
def make_context_current(window: Window):
    _glfw.glfwMakeContextCurrent(window)


_glfw.glfwSwapInterval.restype = None
_glfw.glfwSwapInterval.argtypes = [ctypes.c_int]
def swap_interval(interval: int):
    _glfw.glfwSwapInterval(interval)


_glfw.glfwSwapBuffers.restype = None
_glfw.glfwSwapBuffers.argtypes = [ctypes.POINTER(Window)]
def swap_buffers(window: Window):
    _glfw.glfwSwapBuffers(window)


_glfw.glfwPollEvents.restype = None
_glfw.glfwPollEvents.argtypes = []
def poll_events():
    _glfw.glfwPollEvents()


_glfw.glfwWaitEvents.restype = None
_glfw.glfwWaitEvents.argtypes = []
def wait_events():
    _glfw.glfwWaitEvents()


_glfw.glfwWaitEventsTimeout.restype = None
_glfw.glfwWaitEventsTimeout.argtypes = [ctypes.c_float]
def wait_events_timeout(timeout: float):
    _glfw.glfwWaitEventsTimeout(timeout)


_glfw.glfwIconifyWindow.restype = None
_glfw.glfwIconifyWindow.argtypes = [ctypes.POINTER(Window)]
def iconify_window(window: Window):
    _glfw.glfwIconifyWindow(window)


_glfw.glfwRestoreWindow.restype = None
_glfw.glfwRestoreWindow.argtypes = [ctypes.POINTER(Window)]
def restore_window(window: Window):
    _glfw.glfwRestoreWindow(window)


_glfw.glfwShowWindow.restype = None
_glfw.glfwShowWindow.argtypes = [ctypes.POINTER(Window)]
def show_window(window: Window):
    _glfw.glfwShowWindow(window)


_glfw.glfwHideWindow.restype = None
_glfw.glfwHideWindow.argtypes = [ctypes.POINTER(Window)]
def hide_window(window: Window):
    _glfw.glfwHideWindow(window)


_glfw.glfwMaximizeWindow.restype = None
_glfw.glfwMaximizeWindow.argtypes = [ctypes.POINTER(Window)]
def maximize_window(window: Window):
    _glfw.glfwMaximizeWindow(window)


_glfw.glfwFocusWindow.restype = None
_glfw.glfwFocusWindow.argtypes = [ctypes.POINTER(Window)]
def focus_window(window: Window):
    _glfw.glfwFocusWindow(window)


_glfw.glfwGetFramebufferSize.restype = None
_glfw.glfwGetFramebufferSize.argtypes = [ctypes.POINTER(Window),
                                         ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
def get_framebuffer_size(window: Window) -> (int, int):
    width, height = ctypes.c_int(0), ctypes.c_int(0)
    width_prt, height_ptr = ctypes.pointer(width), ctypes.pointer(height)
    _glfw.glfwGetFramebufferSize(window, width_prt, height_ptr)
    return width.value, height.value


_glfw.glfwGetWindowSize.restype = None
_glfw.glfwSetWindowSize.argtypes = [ctypes.POINTER(Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
def get_window_size(window: Window) -> (int, int):
    width, height = ctypes.c_int(0), ctypes.c_int(0)
    width_prt, height_ptr = ctypes.pointer(width), ctypes.pointer(height)
    _glfw.glfwGetWindowSize(window, width_prt, height_ptr)
    return width.value, height.value


_glfw.glfwSetWindowSize.restype = None
_glfw.glfwSetWindowSize.argtypes = [ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int]
def set_window_size(window: Window, width: int, height: int):
    return _glfw.glfwSetWindowSize(window, width, height)


_glfw.glfwGetWindowPos.restype = None
_glfw.glfwGetWindowPos.argtypes = [ctypes.POINTER(Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
def get_window_pos(window: Window) -> (int, int):
    x, y = ctypes.c_int(0), ctypes.c_int(0)
    x_ptr, y_ptr = ctypes.pointer(x), ctypes.pointer(y)
    _glfw.glfwGetWindowPos(window, x_ptr, y_ptr)
    return x.value, y.value


_glfw.glfwSetWindowPos.restype = None
_glfw.glfwSetWindowPos.argtypes = [ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int]
def set_window_pos(window: Window, x: int, y: int):
    _glfw.glfwSetWindowPos(window, x, y)


_glfw.glfwSetWindowTitle.restype = None
_glfw.glfwSetWindowTitle.argtypes = [ctypes.POINTER(Window), ctypes.c_char_p]
def set_window_title(window: Window, title: str):
    _glfw.glfwSetWindowTitle(window, title.encode())


_glfw.glfwGetKey.restype = ctypes.c_int
_glfw.glfwGetKey.argtypes = [ctypes.POINTER(Window), ctypes.c_int]
def get_key(window: Window, key: int):
    return _glfw.glfwGetKey(window, key)

# ..:: Callbacks ::.. #

# Repository for callback functions,
# to save them from premature garbage collector doom
_CALLBACK_REPOSITORY = {}


_window_pos_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int)
_glfw.glfwSetWindowPosCallback.restype = _window_pos_callback_type
_glfw.glfwSetWindowPosCallback.argtypes = [ctypes.POINTER(Window), _window_pos_callback_type]
def set_window_pos_callback(window: Window, callback: Callable[[Window, int, int], None]):
    _callback = _window_pos_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'window_pos')] = _callback
    _glfw.glfwSetWindowPosCallback(window, _callback)


_window_size_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int)
_glfw.glfwSetWindowSizeCallback.restype = _window_size_callback_type
_glfw.glfwSetWindowSizeCallback.argtypes = [ctypes.POINTER(Window), _window_size_callback_type]
def set_window_size_callback(window: Window, callback: Callable[[Window, int, int], None]):
    _callback = _window_size_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'size')] = _callback
    _glfw.glfwSetWindowSizeCallback(window, _callback)


_framebuffer_size_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int)
_glfw.glfwSetFramebufferSizeCallback.restype = _framebuffer_size_callback_type
_glfw.glfwSetFramebufferSizeCallback.argtypes = [ctypes.POINTER(Window), _framebuffer_size_callback_type]
def set_framebuffer_size_callback(window: Window, callback: Callable[[Window, int, int], None]):
    _callback = _framebuffer_size_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'framebuffer_size')] = _callback
    _glfw.glfwSetFramebufferSizeCallback(window, _callback)


_window_close_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window))
_glfw.glfwSetWindowCloseCallback.restype = _window_close_callback_type
_glfw.glfwSetWindowCloseCallback.argtypes = [ctypes.POINTER(Window), _window_close_callback_type]
def set_window_close_callback(window: Window, callback: Callable[[Window], None]):
    _callback = _window_close_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'close')] = _callback
    _glfw.glfwSetWindowCloseCallback(window, _callback)


_window_refresh_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window))
_glfw.glfwSetWindowRefreshCallback.restype = _window_refresh_callback_type
_glfw.glfwSetWindowRefreshCallback.argtypes = [ctypes.POINTER(Window), _window_refresh_callback_type]
def set_window_refresh_callback(window: Window, callback: Callable[[Window], None]):
    _callback = _window_refresh_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'refresh')] = _callback
    _glfw.glfwSetWindowRefreshCallback(window, _callback)


_window_focus_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int)
_glfw.glfwSetWindowFocusCallback.restype = _window_focus_callback_type
_glfw.glfwSetWindowFocusCallback.argtypes = [ctypes.POINTER(Window), _window_focus_callback_type]
def set_window_focus_callback(window: Window, callback: Callable[[Window, int], None]):
    _callback = _window_focus_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'focus')] = _callback
    _glfw.glfwSetWindowFocusCallback(window, _callback)


_window_iconify_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int)
_glfw.glfwSetWindowIconifyCallback.restype = _window_iconify_callback_type
_glfw.glfwSetWindowIconifyCallback.argtypes = [ctypes.POINTER(Window), _window_iconify_callback_type]
def set_window_iconify_callback(window: Window, callback: Callable[[Window, int], None]):
    _callback = _window_iconify_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'iconify')] = _callback
    _glfw.glfwSetWindowIconifyCallback(window, _callback)


_key_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
_glfw.glfwSetKeyCallback.restype = _key_callback_type
_glfw.glfwSetKeyCallback.argtypes = [ctypes.POINTER(Window), _key_callback_type]
def set_key_callback(window: Window, callback: Callable[[Window, int, int, int, int], None]):
    _callback = _key_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'key')] = _callback
    _glfw.glfwSetKeyCallback(window, _callback)


_char_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_uint)
_glfw.glfwSetCharCallback.restype = _char_callback_type
_glfw.glfwSetCharCallback.argtypes = [ctypes.POINTER(Window), _char_callback_type]
def set_char_callback(window: Window, callback: Callable[[Window, int], None]):
    _callback = _char_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'char')] = _callback
    _glfw.glfwSetCharCallback(window, _callback)


_cursor_pos_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_double, ctypes.c_double)
_glfw.glfwSetCursorPosCallback.restype = _cursor_pos_callback_type
_glfw.glfwSetCursorPosCallback.argtypes = [ctypes.POINTER(Window), _cursor_pos_callback_type]
def set_cursor_pos_callback(window: Window, callback: Callable[[Window, float, float], None]):
    _callback = _cursor_pos_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'cursor_pos')] = _callback
    _glfw.glfwSetCursorPosCallback(window, _callback)


_mouse_button_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_int, ctypes.c_int, ctypes.c_int)
_glfw.glfwSetMouseButtonCallback.restype = _mouse_button_callback_type
_glfw.glfwSetMouseButtonCallback.argtypes = [ctypes.POINTER(Window), _mouse_button_callback_type]
def set_mouse_button_callback(window: Window, callback: Callable[[Window, int, int, int], None]):
    _callback = _mouse_button_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'mouse_button')] = _callback
    _glfw.glfwSetMouseButtonCallback(window, _callback)


_scroll_callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(Window), ctypes.c_double, ctypes.c_double)
_glfw.glfwSetScrollCallback.restype = _scroll_callback_type
_glfw.glfwSetScrollCallback.argtypes = [ctypes.POINTER(Window), _scroll_callback_type]
def set_scroll_callback(window: Window, callback: Callable[[Window, float, float], None]):
    _callback = _scroll_callback_type(callback)
    _CALLBACK_REPOSITORY["{}{}".format(window[0].id, 'scroll')] = _callback
    _glfw.glfwSetScrollCallback(window, _callback)
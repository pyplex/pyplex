from pyplex import *
from ctypes import *
import numpy as np
from sys import stderr

from threading import Thread
from typing import List, Optional
from enum import Enum


class GLError(Exception):
    pass


class VideoMode:
    def __init__(self, mode: glfw.VideoMode):
        self._resolution = np.array([mode.width, mode.height])
        self._bit_depth = np.array([mode.red_bits, mode.green_bits, mode.blue_bits])
        self._refresh_rate = mode.refresh_rate

    @property
    def width(self) -> int:
        return self._resolution[0]

    @property
    def height(self) -> int:
        return self._resolution[1]

    @property
    def resolution(self) -> np.ndarray:
        return self._resolution

    @property
    def bit_depth(self) -> np.ndarray:
        return self._bit_depth

    @property
    def refresh_rate(self) -> int:
        return self._refresh_rate

    def __str__(self):
        return "{}x{}@{}Hz".format(self.width, self.height, self.refresh_rate)


class Monitor:
    def __init__(self, monitor: glfw.Monitor):
        self._monitor = monitor

    @property
    def position(self) -> np.ndarray:
        position = np.empty(2, np.int)
        Canvas.GLFW.get_monitor_pos(self._monitor,
                                    cast(position.ctypes.data, POINTER(c_int)),
                                    cast(position.ctypes.data + sizeof(c_int), POINTER(c_int)))
        return position

    @property
    def size(self) -> np.ndarray:
        size = np.empty(2, np.int)
        Canvas.GLFW.get_monitor_physical_size(self._monitor,
                                              cast(size.ctypes.data, POINTER(c_int)),
                                              cast(size.ctypes.data + sizeof(c_int), POINTER(c_int)))
        return size

    @property
    def name(self) -> str:
        return Canvas.GLFW.get_monitor_name(self._monitor).decode()

    @property
    def video_mode(self) -> VideoMode:
        return VideoMode(Canvas.GLFW.get_video_mode(self._monitor)[0])

    @property
    def video_modes(self) -> List[VideoMode]:
        count = c_int(0)
        video_modes = Canvas.GLFW.get_video_modes(self._monitor, pointer(count))
        return [VideoMode(video_modes[i]) for i in range(count.value)]

    @property
    def gamma_ramp(self) -> np.ndarray:
        ramp = Canvas.GLFW.get_gamma_ramp(self._monitor)[0]
        return np.concatenate([
            (np.ctypeslib.as_array(ramp.red, (ramp.size, 1))),
            (np.ctypeslib.as_array(ramp.green, (ramp.size, 1))),
            (np.ctypeslib.as_array(ramp.blue, (ramp.size, 1)))], axis=1)

    @gamma_ramp.setter
    def gamma_ramp(self, value: np.ndarray):
        if not (value.dtype == np.uint16 and value.shape == (256, 3)):
            raise ValueError("Gamma Ramp should be in format uint16[256, 3]")

        Canvas.GLFW.set_gamma_ramp(
            self._monitor,
            glfw.GammaRamp(
                value[:, 0].ctypes.data_as(POINTER(c_ushort)),
                value[:, 1].ctypes.data_as(POINTER(c_ushort)),
                value[:, 2].ctypes.data_as(POINTER(c_ushort)),
                value.shape[0]))

    def set_gamma(self, gamma: float):
        Canvas.GLFW.set_gamma(self._monitor, gamma)


class Cursor:
    def __init__(self, cursor: glfw.Cursor):
        self._cursor = cursor

    @property
    def cursor(self):
        return self._cursor


class ImageCursor(Cursor):
    def __init__(self, image: np.ndarray, hotspot: np.ndarray):
        super().__init__(Canvas.GLFW.create_cursor(
            glfw.Image(image.shape[0], image.shape[1], image.ctypes.data_as(POINTER(c_ubyte))),
            hotspot[0],
            hotspot[1]))


class StandardCursor(Cursor):
    def __init__(self, shape: CursorShape):
        super().__init__(Canvas.GLFW.create_standard_cursor(shape))

    @property
    def cursor(self) -> glfw.Cursor:
        return self._cursor


class ArrowCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.ARROW)


class IBeamCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.IBEAM)


class CrosshairCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.CROSSHAIR)


class HandCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.HAND)


class HResizeCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.HRESIZE)


class VResizeCursor(StandardCursor):
    def __init__(self):
        super().__init__(CursorShape.VRESIZE)


class CanvasEventFunction(Enum):
    POLL = 0
    WAIT = 1


class CanvasConfig:
    def __init__(self, width: int=1024, height: int=768, title: str="pyplex", context_type=gl.GL43,
                 resizable: bool=True, visible: bool=True, decorated: bool=True, focused: bool=True,
                 floating: bool=False, maximised: bool=False, auto_iconify: bool=True, vsync: int=1,
                 red: int=8, green: int=8, blue: int=8, alpha: int=8, depth: int=24, stencil: int=8,
                 double_buffer: bool=True, samples: int=0, stereo: bool=False, srgb: bool=False,
                 event_function: CanvasEventFunction = CanvasEventFunction.POLL):

        super().__init__()

        self._width = width
        self._height = height
        self._title = title
        self._context_type = context_type
        self._resizable = resizable
        self._visible = visible
        self._decorated = decorated
        self._focused = focused
        self._floating = floating
        self._maximized = maximised
        self._auto_iconify = auto_iconify
        self._vsync = vsync
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha
        self._depth = depth
        self._stencil = stencil
        self._double_buffer = double_buffer
        self._samples = samples
        self._stereo = stereo
        self._srgb = srgb
        self._event_function = event_function

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def title(self) -> str:
        return self._title

    @property
    def context_type(self):
        return self._context_type

    @property
    def resizable(self) -> bool:
        return self._resizable

    @property
    def visible(self) -> bool:
        return self._visible

    @property
    def decorated(self) -> bool:
        return self._decorated

    @property
    def focused(self) -> bool:
        return self._focused

    @property
    def floating(self) -> bool:
        return self._floating

    @property
    def maximised(self) -> bool:
        return self._maximized

    @property
    def auto_iconify(self) -> bool:
        return self._auto_iconify

    @property
    def vsync(self) -> int:
        return self._vsync

    @property
    def red(self) -> int:
        return self._red

    @property
    def green(self) -> int:
        return  self._green

    @property
    def blue(self) -> int:
        return self._blue

    @property
    def alpha(self) -> int:
        return self._alpha

    @property
    def depth(self) -> int:
        return self._depth

    @property
    def stencil(self) -> int:
        return self._stencil

    @property
    def double_buffer(self) -> bool:
        return self._double_buffer

    @property
    def samples(self) -> int:
        return self._samples

    @property
    def stereo(self) -> bool:
        return self._stereo

    @property
    def srgb(self) -> bool:
        return self._srgb

    @property
    def event_function(self) -> CanvasEventFunction:
        return self._event_function


class Canvas:

    COUNT = 0
    GLFW = None

    def __init__(self, config: CanvasConfig=CanvasConfig()):
        self._config = config

        self._title = self._config.title

        if not Canvas.GLFW:
            Canvas.GLFW = glfw.GLFW()
            Canvas.GLFW.init()
        Canvas.COUNT += 1

        self._event_function = Canvas.GLFW.poll_events \
            if self._config.event_function == CanvasEventFunction.POLL \
            else Canvas.GLFW.wait_events

        self._initialized = False

    @property
    def monitor(self) -> Monitor:
        return Monitor(Canvas.GLFW.get_primary_monitor())

    @property
    def monitors(self) -> List[Monitor]:
        count = c_int(0)
        monitors = Canvas.GLFW.get_monitors(pointer(count))
        return [Monitor(monitors[i]) for i in range(count.value)]

    @property
    def should_close(self) -> bool:
        return Canvas.GLFW.window_should_close(self._window)

    @should_close.setter
    def should_close(self, value: bool):
        Canvas.GLFW.set_window_should_close(self._window, value)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        Canvas.GLFW.set_window_title(self._window, value.encode())
        self._title = value

    @property
    def position(self) -> np.ndarray:
        pos = np.empty(2, np.int)
        Canvas.GLFW.get_window_pos(self._window,
                                   cast(pos.ctypes.data, POINTER(c_int)),
                                   cast(pos.ctypes.data + sizeof(c_int), POINTER(c_int)))
        return pos

    @position.setter
    def position(self, value: np.ndarray):
        Canvas.GLFW.set_window_pos(self._window, value[0], value[1])

    @property
    def size(self) -> np.ndarray:
        size = np.empty(2, np.int)
        Canvas.GLFW.get_window_size(self._window,
                                    cast(size.ctypes.data, POINTER(c_int)),
                                    cast(size.ctypes.data + sizeof(c_int), POINTER(c_int)))
        return size

    @size.setter
    def size(self, value: np.ndarray):
        Canvas.GLFW.set_window_size(self._window, value[0], value[1])

    @property
    def framebuffer_size(self) -> np.ndarray:
        size = np.empty(2, np.int)
        Canvas.GLFW.get_framebuffer_size(self._window,
                                         cast(size.ctypes.data, POINTER(c_int)),
                                         cast(size.ctypes.data + sizeof(c_int), POINTER(c_int)))
        return size

    @property
    def frame_size(self) -> np.ndarray:
        size = np.empty((4), np.int)
        Canvas.GLFW.get_window_frame_size(self._window,
                                          cast(size.ctypes.data                     , POINTER(c_int)),
                                          cast(size.ctypes.data +     sizeof(c_int) , POINTER(c_int)),
                                          cast(size.ctypes.data + 2 * sizeof(c_int) , POINTER(c_int)),
                                          cast(size.ctypes.data + 3 * sizeof(c_int) , POINTER(c_int)))
        return size

    @property
    def mouse_position(self) -> np.ndarray:
        pos = np.empty(2, np.double)
        Canvas.GLFW.get_cursor_pos(self._window,
                                   cast(pos.ctypes.data, POINTER(c_int)),
                                   cast(pos.ctypes.data + sizeof(c_double), POINTER(c_int)))
        return pos

    @mouse_position.setter
    def mouse_position(self, value: np.ndarray):
        Canvas.GLFW.set_cursor_pos(self._window, value[0], value[1])

    @property
    def cursor_mode(self) -> CursorMode:
        return CursorMode(Canvas.GLFW.get_input_mode(self._window, glfw.CURSOR))

    @cursor_mode.setter
    def cursor_mode(self, value: CursorMode):
        Canvas.GLFW.set_input_mode(self._window, glfw.CURSOR, value)

    @property
    def sticky_keys(self) -> bool:
        return bool(Canvas.GLFW.get_input_mode(self._window, glfw.STICKY_KEYS))

    @sticky_keys.setter
    def sticky_keys(self, value: bool):
        Canvas.GLFW.set_input_mode(self._window, glfw.STICKY_KEYS, value)

    @property
    def sticky_mouse_buttons(self) -> bool:
        return bool(Canvas.GLFW.get_input_mode(self._window, glfw.STICKY_MOUSE_BUTTONS))

    @sticky_mouse_buttons.setter
    def sticky_mouse_buttons(self, value: bool):
        Canvas.GLFW.set_input_mode(self._window, glfw.STICKY_MOUSE_BUTTONS, value)

    @property
    def clipboard(self) -> str:
        return Canvas.GLFW.get_clipboard_string(self._window).decode()

    @clipboard.setter
    def clipboard(self, value: str):
        Canvas.GLFW.set_clipboard_string(self._window, value.encode())

    def get_key(self, key: Key) -> Action:
        return Action(Canvas.GLFW.get_key(self._window, key))

    def get_mouse_button(self, button: Button) -> Action:
        return Action(Canvas.GLFW.get_mouse_button(self._window, button))

    def set_size_limits(self, width_min: int, height_min: int, width_max: int, height_max: int):
        Canvas.GLFW.set_window_size_limits(self._window, width_min, height_min, width_max, height_max)

    def set_aspect_ratio(self, numerator: int, denominator: int):
        Canvas.GLFW.set_window_aspect_ratio(self._window, numerator, denominator)

    def set_icon(self, *value: np.ndarray):
        glfw_images = (glfw.Image * len(value))()

        for i, image in enumerate(value):
            glfw_images[i].width = image.shape[0]
            glfw_images[i].height = image.shape[1]
            glfw_images[i].pixels = image.ctypes.data_as(POINTER(c_ubyte))

        self.GLFW.set_window_icon(self._window, len(value), glfw_images)
        self._icons = value

    def set_cursor(self, cursor: Optional[Cursor]):
        Canvas.GLFW.set_cursor(self._window, cursor.cursor if cursor else None)

    def set_event_function(self, event_function: CanvasEventFunction):
        self._event_function = Canvas.GLFW.poll_events \
            if event_function == CanvasEventFunction.POLL \
            else Canvas.GLFW.wait_events

    def iconify(self):
        Canvas.GLFW.iconify_window(self._window)

    def restore(self):
        Canvas.GLFW.restore_window(self._window)

    def maximize(self):
        Canvas.GLFW.maximize_window(self._window)

    def show(self):
        Canvas.GLFW.show_window(self._window)

    def hide(self):
        Canvas.GLFW.hide_window(self._window)

    def focus(self):
        Canvas.GLFW.focus_window(self._window)

    def start(self):
        Thread(target=self.run).start()

    def run(self):
        # Create Window
        self._set_window_hints()
        self._window = Canvas.GLFW.create_window(
            self._config.width, self._config.height,self._config.title.encode(), None, None)
        Canvas.GLFW.default_window_hints()

        # Create Context
        Canvas.GLFW.make_context_current(self._window)
        Canvas.GLFW.swap_interval(self._config.vsync)
        context = self._config.context_type(Canvas.GLFW)

        self._set_callbacks()

        gl_error_callback_type = CFUNCTYPE(None, c_uint, c_uint, c_uint, c_uint, c_uint, c_char_p, c_void_p)
        gl_error_callback = gl_error_callback_type(self._gl_error_callback)

        context.enable(0x92E0)  # Enable GL Debug Output
        context.debug_message_callback(gl_error_callback, c_void_p(0))

        self._initialized = True

        self.on_start(context)

        if self._config.visible: self.show()

        while not Canvas.GLFW.window_should_close(self._window):

            self.on_update()
            self.on_draw()

            Canvas.GLFW.swap_buffers(self._window)
            self._event_function()

        Canvas.GLFW.destroy_window(self._window)

        Canvas.COUNT -= 1
        if Canvas.COUNT == 0:
            Canvas.GLFW.terminate()

    def on_start(self, ctx: gl.GL_ANY):
        pass

    def on_update(self):
        pass

    def on_draw(self):
        pass

    def on_move(self, x: int, y: int):
        pass

    def on_resize(self, width: int, height: int):
        pass

    def on_framebuffer_resize(self, width: int, height: int):
        pass

    def on_close(self):
        pass

    def on_refresh(self):
        pass

    def on_focus(self, value: bool):
        pass

    def on_iconify(self, value: bool):
        pass

    def on_mouse_button(self, button: Button, action: Action, modifiers: Modifiers):
        pass

    def on_mouse_move(self, x: float, y: float):
        pass

    def on_mouse_enter(self, value: bool):
        pass

    def on_scroll(self, x: float, y: float):
        pass

    def on_key(self, key: Key, action: Action, modifiers: Modifiers):
        pass

    def on_char(self, char: str):
        pass

    def on_char_mods(self, char: str, modifiers: Modifiers):
        pass

    def on_drop(self, paths: List[str]):
        pass

    def on_joystick(self, joy: int, event: ConnectionEvent):
        pass

    def on_monitor(self, monitor: glfw.Monitor, event: ConnectionEvent):
        pass

    def _on_move(self, window: glfw.Window, x: int, y: int):
        self.on_move(x, y)

    def _on_resize(self, window: glfw.Window, width: int, height: int):
        self.on_resize(width, height)

    def _on_framebuffer_resize(self, window: glfw.Window, width: int, height: int):
        self.on_framebuffer_resize(width, height)

    def _on_close(self, window: glfw.Window):
        self.on_close()

    def _on_refresh(self, window: glfw.Window):
        self.on_refresh()

    def _on_focus(self, window: glfw.Window, value: int):
        self.on_focus(bool(value))

    def _on_iconify(self, window: glfw.Window, value: int):
        self.on_iconify(bool(value))

    def _on_mouse_button(self, window: glfw.Window, button: int, action: int, modifier: int):
        self.on_mouse_button(Button(button), Action(action), Modifiers(modifier))

    def _on_mouse_move(self, window: glfw.Window, x: float, y: float):
        self.on_mouse_move(x, y)

    def _on_mouse_enter(self, window: glfw.Window, value: int):
        self.on_mouse_enter(bool(value))

    def _on_scroll(self, window: glfw.Window, x: float, y: float):
        self.on_scroll(x, y)

    def _on_key(self, window: glfw.Window, key: int, scancode: int, action: int, modifiers: int):
        return self.on_key(Key(key), Action(action), Modifiers(modifiers))

    def _on_char(self, window: glfw.Window, code: int):
        self.on_char(chr(code))

    def _on_char_mods(self, window: glfw.Window, code: int, modifiers: int):
        self.on_char_mods(chr(code), Modifiers(modifiers))

    def _on_drop(self, window: glfw.Window, count: int, paths: POINTER(c_char_p)):
        self.on_drop([paths[i].decode() for i in range(count)])

    def _on_joystick(self, joy: int, event: int):
        self.on_joystick(joy, ConnectionEvent(event))

    def _on_monitor(self, monitor: glfw.Monitor, event: int):
        self.on_monitor(monitor, ConnectionEvent(event))

    def _set_callbacks(self):
        self._on_move = Canvas.GLFW.WINDOW_POSITION_CALLBACK(self._on_move)
        self._on_resize = Canvas.GLFW.WINDOW_SIZE_CALLBACK(self._on_resize)
        self._on_framebuffer_resize = Canvas.GLFW.FRAMEBUFFER_SIZE_CALLBACK(self._on_framebuffer_resize)

        self._on_close = Canvas.GLFW.WINDOW_CLOSE_CALLBACK(self._on_close)
        self._on_refresh = Canvas.GLFW.WINDOW_REFRESH_CALLBACK(self._on_refresh)
        self._on_focus = Canvas.GLFW.WINDOW_FOCUS_CALLBACK(self._on_focus)
        self._on_iconify = Canvas.GLFW.WINDOW_ICONIFY_CALLBACK(self._on_iconify)

        self._on_mouse_button = Canvas.GLFW.MOUSE_BUTTON_CALLBACK(self._on_mouse_button)
        self._on_mouse_move = Canvas.GLFW.CURSOR_POSITION_CALLBACK(self._on_mouse_move)
        self._on_mouse_enter = Canvas.GLFW.CURSOR_ENTER_CALLBACK(self._on_mouse_enter)
        self._on_scroll = Canvas.GLFW.SCROLL_CALLBACK(self._on_scroll)

        self._on_key = Canvas.GLFW.KEY_CALLBACK(self._on_key)
        self._on_char = Canvas.GLFW.CHAR_CALLBACK(self._on_char)
        self._on_char_mods = Canvas.GLFW.CHAR_MODS_CALLBACK(self._on_char_mods)

        self._on_drop = Canvas.GLFW.DROP_CALLBACK(self._on_drop)

        self._on_joystick = Canvas.GLFW.JOYSTICK_CALLBACK(self._on_joystick)
        self._on_monitor = Canvas.GLFW.MONITOR_CALLBACK(self._on_monitor)

        Canvas.GLFW.set_window_pos_callback(self._window, self._on_move)
        Canvas.GLFW.set_window_size_callback(self._window, self._on_resize)
        Canvas.GLFW.set_framebuffer_size_callback(self._window, self._on_framebuffer_resize)

        Canvas.GLFW.set_window_close_callback(self._window, self._on_close)
        Canvas.GLFW.set_window_refresh_callback(self._window, self._on_refresh)
        Canvas.GLFW.set_window_focus_callback(self._window, self._on_focus)
        Canvas.GLFW.set_window_iconify_callback(self._window, self._on_iconify)

        Canvas.GLFW.set_mouse_button_callback(self._window, self._on_mouse_button)
        Canvas.GLFW.set_cursor_pos_callback(self._window, self._on_mouse_move)
        Canvas.GLFW.set_cursor_enter_callback(self._window, self._on_mouse_enter)
        Canvas.GLFW.set_scroll_callback(self._window, self._on_scroll)

        Canvas.GLFW.set_key_callback(self._window, self._on_key)
        Canvas.GLFW.set_char_callback(self._window, self._on_char)
        Canvas.GLFW.set_char_mods_callback(self._window, self._on_char_mods)

        Canvas.GLFW.set_drop_callback(self._window, self._on_drop)

        Canvas.GLFW.set_joystick_callback(self._on_joystick)
        Canvas.GLFW.set_monitor_callback(self._on_monitor)

    def _set_window_hints(self):
        Canvas.GLFW.window_hint(glfw.CONTEXT_VERSION_MAJOR, self._config.context_type.MAJOR)
        Canvas.GLFW.window_hint(glfw.CONTEXT_VERSION_MINOR, self._config.context_type.MINOR)
        Canvas.GLFW.window_hint(glfw.CLIENT_API, glfw.OPENGL_API)
        Canvas.GLFW.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        Canvas.GLFW.window_hint(glfw.OPENGL_DEBUG_CONTEXT, False)

        Canvas.GLFW.window_hint(glfw.RESIZABLE, self._config.resizable)
        Canvas.GLFW.window_hint(glfw.VISIBLE, False)  # Will be set after on_start()
        Canvas.GLFW.window_hint(glfw.DECORATED, self._config.decorated)
        Canvas.GLFW.window_hint(glfw.FOCUSED, self._config.focused)
        Canvas.GLFW.window_hint(glfw.FLOATING, self._config.floating)
        Canvas.GLFW.window_hint(glfw.MAXIMIZED, self._config.maximised)
        Canvas.GLFW.window_hint(glfw.AUTO_ICONIFY, self._config.auto_iconify)

        Canvas.GLFW.window_hint(glfw.RED_BITS, self._config.red)
        Canvas.GLFW.window_hint(glfw.GREEN_BITS, self._config.green)
        Canvas.GLFW.window_hint(glfw.BLUE_BITS, self._config.blue)
        Canvas.GLFW.window_hint(glfw.ALPHA_BITS, self._config.alpha)
        Canvas.GLFW.window_hint(glfw.DEPTH_BITS, self._config.depth)
        Canvas.GLFW.window_hint(glfw.STENCIL_BITS, self._config.stencil)
        Canvas.GLFW.window_hint(glfw.SAMPLES, self._config.samples)
        Canvas.GLFW.window_hint(glfw.STEREO, self._config.stereo)
        Canvas.GLFW.window_hint(glfw.SRGB_CAPABLE, self._config.srgb)
        Canvas.GLFW.window_hint(glfw.DOUBLEBUFFER, self._config.double_buffer)

    def _gl_error_callback(self, source: int, type: int, id: int, severity: int,
                           length: int, message: bytes, user_param: c_void_p):

        if severity == gl.DebugSeverity.HIGH:
            raise GLError("{} {} ({})\n\t{}".format(
                gl.DebugSource(source).name,
                gl.DebugType(type).name,
                id, message.decode()))
        elif severity == gl.DebugSeverity.MEDIUM or severity == gl.DebugSeverity.LOW:
            print("{} {} Warning ({})\n\t{}".format(
                gl.DebugSource(source).name,
                gl.DebugType(type).name,
                id,
                message.decode()), file=stderr)
        else:
            print("{} {} Notification ({})\n\t{}".format(
                gl.DebugSource(source).name,
                gl.DebugType(type).name,
                id,
                message.decode()))


class VerboseCanvas(Canvas):
    def on_start(self, ctx: gl.GL_ANY):
        print("on_start({})".format(ctx))

    def on_update(self):
        print("on_update()")

    def on_draw(self):
        print("on_draw()")

    def on_move(self, x: int, y: int):
        print("on_move(x: {}, y: {})".format(x, y))

    def on_resize(self, width: int, height: int):
        print("on_resize(width: {}, height: {})".format(width, height))

    def on_framebuffer_resize(self, width: int, height: int):
        print("on_framebuffer_resize(width: {}, height: {})".format(width, height))

    def on_close(self):
        print("on_close()")

    def on_refresh(self):
        print("on_refresh()")

    def on_focus(self, value: bool):
        print("on_focus(value: {})".format(value))

    def on_iconify(self, value: bool):
        print("on_iconify(value: {})".format(value))

    def on_mouse_button(self, button: Button, action: Action, modifiers: Modifiers):
        print("on_mouse_button(button: {}, action: {}, modifiers: {})".format(button, action, modifiers))

    def on_mouse_move(self, x: float, y: float):
        print("on_mouse_move(x: {}, y: {})".format(x, y))

    def on_mouse_enter(self, value: bool):
        print("on_mouse_enter(value: {})".format(value))

    def on_scroll(self, x: float, y: float):
        print("on_scroll(x: {}, y: {})".format(x, y))

    def on_key(self, key: Key, action: Action, modifiers: Modifiers):
        print("on_key(key: {}, action: {}, modifiers: {})".format(key, action, modifiers))

    def on_char(self, char: str):
        print("on_char(char: {})".format(char))

    def on_char_mods(self, char: str, modifiers: Modifiers):
        print("on_char_mods(char: {}, modifiers: {})".format(char, modifiers))

    def on_drop(self, paths: List[str]):
        print("on_drop(paths: {})".format(paths))

    def on_joystick(self, joy: int, event: ConnectionEvent):
        print("on_joystick(joy: {}, event: {})".format(joy, event))

    def on_monitor(self, monitor: glfw.Monitor, event: ConnectionEvent):
        print("on_monitor(monitor: {}, event: {})".format(monitor, event))

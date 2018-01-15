from pyplex import gl, glfw, VERSION_GL, Key, Button, Action, Modifier

import numpy as np

from time import time
from typing import List, Optional


class VideoMode:
    def __init__(self, video_mode: glfw.VideoMode):
        """
        Supported video mode for monitor

        Parameters
        ----------
        video_mode: pyplex.glfw.VideoMode
            GLFW VideoMode object
        """

        self._resolution = np.array([video_mode.width, video_mode.height], np.uint32)
        self._bit_depth = np.array([video_mode.red_bits, video_mode.green_bits, video_mode.blue_bits], np.uint8)
        self._refresh_rate = video_mode.refresh_rate

    @property
    def resolution(self) -> np.ndarray:
        """
        VideoMode resolution (w,h) in pixels

        Returns
        -------
        resolution: np.ndarray
        """
        return self._resolution

    @property
    def width(self) -> int:
        """
        VideoMode width in pixels

        Returns
        -------
        width: int
        """
        return self._resolution[0]

    @property
    def height(self) -> int:
        """
        VideoMode height in pixels

        Returns
        -------
        height: int
        """
        return self._resolution[1]

    @property
    def bit_depth(self) -> np.ndarray:
        """
        VideoMode bit depth (r,g,b)

        Returns
        -------
        bit_depth: np.ndarray
        """
        return self._bit_depth

    @property
    def refresh_rate(self) -> int:
        """
        VideoMode refresh rate

        Returns
        -------
        refresh_rate: int
        """
        return self._refresh_rate

    def __str__(self):
        """
        String representation of VideoMode: <width>x<height>@<refresh_rate>Hz

        Returns
        -------
        __str__: str
        """
        return "{}x{}@{}Hz".format(self.width, self.height, self.refresh_rate)


class Monitor:
    def __init__(self, monitor: glfw.Monitor):
        """
        Currently connected monitor

        Parameters
        ----------
        monitor: pyplex.glfw.Monitor
            GLFW Monitor object
        """
        self._monitor = monitor

    @classmethod
    def primary(cls):
        """
        Retrieve primary monitor

        Returns
        -------
        monitor: Monitor
        """
        return cls(glfw.get_primary_monitor())

    @staticmethod
    def monitors() -> list:
        """
        Retrieve all connected monitors

        Returns
        -------
        monitors: list of Monitor
        """
        return [Monitor(monitor) for monitor in glfw.get_monitors()]

    @property
    def name(self) -> str:
        """
        Human-readable monitor name

        Returns
        -------
        name: str
        """
        return glfw.get_monitor_name(self._monitor)

    @property
    def position(self) -> np.ndarray:
        """
        Monitor position (x,y) in screen coordinates

        see: http://www.glfw.org/docs/latest/intro_guide.html#coordinate_systems

        Returns
        -------
        position: np.ndarray
        """
        return np.array(glfw.get_monitor_pos(self._monitor), np.int32)

    @property
    def physical_size(self) -> np.ndarray:
        """
        Monitor physical size (w,h) in millimetres

        Returns
        -------
        physical_size: np.ndarray
        """
        return np.array(glfw.get_monitor_physical_size(self._monitor), np.int32)

    @property
    def video_mode(self) -> VideoMode:
        """
        Current video mode of monitor

        Returns
        -------
        mode: VideoMode
        """
        return VideoMode(glfw.get_video_mode(self._monitor))

    @property
    def video_modes(self) -> List[VideoMode]:
        """
        Supported video modes of monitor

        Returns
        -------
        modes: list of VideoMode
        """
        return [VideoMode(video_mode) for video_mode in glfw.get_video_modes(self._monitor)]

    def __str__(self):
        """
        String representation of monitor: <name> : <video_mode>

        Returns
        -------
        __str__: str
        """
        return "{} : {}".format(self.name, self.video_mode)


class Canvas:

    COUNT = 0

    def __init__(self, width: int = 1024, height: int = 768, title: str = "pyplex", version: (int, int) = VERSION_GL,
                 resizable: bool = True, visible: bool = True, decorated: bool = True, focused: bool = True,
                 floating: bool = False, maximised: bool = False, auto_iconify: bool = True, vsync: int = 1,
                 red: int = 8, green: int = 8, blue: int = 8, alpha: int = 8, depth: int = 24, stencil: int = 8,
                 double_buffer: bool = True, samples: int = 0, stereo: bool = False, sRGB: bool = False,
                 wait_for_events: bool = False):
        """
        Create Canvas: (Window + OpenGL Context)

        Parameters
        ----------
        width: int
            Width of Canvas in pixels
        height: int
            Height of Canvas in pixels
        title: str
            Title of Canvas
        version: (int, int)
            OpenGL version of Context
        resizable: bool
            Whether Window will be resizable by the user
        visible: bool
            Whether Window will be initially visible
        decorated: bool
            Whether Window is decorated (i.e. border + close/minimize/maximize buttons)
        focused: bool
            Whether Window will be given input focus
        floating: bool
            Whether Window will be 'always-on-top'
        maximised: bool
            Whether window will be maximised at creation
        auto_iconify: bool
            Whether video mode will be restored on full screen Window input focus loss
        vsync: int
            Number of screen updates to wait before drawing
        red: int
            Number of red bits
        green: int
            Number of green bits
        blue: int
            Number of blue bits
        alpha: int
            Number of alpha bits
        depth: int
            Number of depth bits
        stencil: int
            Number of stencil bits
        double_buffer: bool
            Whether to use double buffering
        samples: int
            Number of samples for multisampling (0 disables multisampling)
        stereo: bool
            Whether to use stereoscopic rendering
        sRGB: bool
            Whether framebuffer should support sRGB
        wait_for_events: bool
            Whether to wait for events to update or update continuously
        wait_events_timeout: optional float
            If wait_events, update at timeout
        """

        # if this Canvas is the first: initialize GLFW
        if Canvas.COUNT == 0: glfw.init()
        Canvas.COUNT += 1

        # OpenGL Context hints
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, version[0])
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, version[1])
        glfw.window_hint(glfw.CLIENT_API, glfw.OPENGL_API)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_DEBUG_CONTEXT, False)

        # Window hints
        glfw.window_hint(glfw.RESIZABLE, resizable)
        glfw.window_hint(glfw.VISIBLE, visible)
        glfw.window_hint(glfw.DECORATED, decorated)
        glfw.window_hint(glfw.FOCUSED, focused)
        glfw.window_hint(glfw.FLOATING, floating)
        glfw.window_hint(glfw.MAXIMIZED, maximised)
        glfw.window_hint(glfw.AUTO_ICONIFY, auto_iconify)

        # Framebuffer hints
        glfw.window_hint(glfw.RED_BITS, red)
        glfw.window_hint(glfw.GREEN_BITS, green)
        glfw.window_hint(glfw.BLUE_BITS, blue)
        glfw.window_hint(glfw.ALPHA_BITS, alpha)
        glfw.window_hint(glfw.DEPTH_BITS, depth)
        glfw.window_hint(glfw.STENCIL_BITS, stencil)
        glfw.window_hint(glfw.SAMPLES, samples)
        glfw.window_hint(glfw.STEREO, stereo)
        glfw.window_hint(glfw.SRGB_CAPABLE, sRGB)
        glfw.window_hint(glfw.DOUBLEBUFFER, double_buffer)

        self._title = title
        self._vsync = vsync

        # Create GLFW Window object and create Context for this thread
        self._window = glfw.create_window(width, height, title, None, None)
        glfw.make_context_current(self._window)
        glfw.swap_interval(vsync)
        glfw.default_window_hints()

        # Event Processing Function
        self._event_processing_func = glfw.wait_events if wait_for_events else glfw.poll_events

        # Initialize Context (i.e. load function pointers)
        self._ctx = gl.Context()

        # Statistics
        self._time_last_frame = time()
        self._time_update = 0
        self._time_draw = 0
        self._time_frame = 0

        # Window Callbacks
        glfw.set_window_pos_callback(self._window, self._on_move)
        glfw.set_window_size_callback(self._window, self._on_resize)
        glfw.set_window_close_callback(self._window, self._on_close)
        glfw.set_window_refresh_callback(self._window, self._on_refresh)
        glfw.set_window_focus_callback(self._window, self._on_focus)
        glfw.set_framebuffer_size_callback(self._window, self._on_framebuffer_resize)

        # Input Callbacks
        glfw.set_key_callback(self._window, self._on_key)
        glfw.set_char_callback(self._window, self._on_char)
        glfw.set_cursor_pos_callback(self._window, self._on_mouse_move)
        glfw.set_mouse_button_callback(self._window, self._on_mouse_button)
        glfw.set_scroll_callback(self._window, self._on_scroll)

    @property
    def ctx(self) -> gl.Context:
        """
        Get Context

        Returns
        -------
        context: pyplex.gl.Context
        """
        return self._ctx

    @property
    def size(self) -> np.ndarray:
        # TODO: Check if size is really in pixels! (Maybe it is in GLFW screen coordinates)
        """
        Get Window size (w,h) in pixels

        Returns
        -------
        size: np.ndarray
        """
        return np.array(glfw.get_window_size(self._window), np.uint32)

    @size.setter
    def size(self, value: np.ndarray):
        """
        Set window size (w,h) in pixels

        Parameters
        ----------
        value: np.ndarray
        """
        glfw.set_window_size(self._window, value[0], value[1])

    @property
    def width(self) -> int:
        """
        Get Window width in pixels

        Returns
        -------
        width: int
        """
        return self.size[0]

    @width.setter
    def width(self, value: int):
        """
        Set Window width in pixels

        Parameters
        ----------
        value: int
        """
        glfw.set_window_size(self._window, value, self.height)

    @property
    def height(self) -> int:
        """
        Get Window height in pixels

        Returns
        -------
        height: int
        """
        return self.size[1]

    @height.setter
    def height(self, value: int):
        """
        Set Window height in pixels

        Parameters
        ----------
        value: int
        """
        glfw.set_window_size(self._window, self.width, value)

    @property
    def framebuffer_size(self) -> np.ndarray:
        """
        Get framebuffer size (w,h) in pixels

        Returns
        -------
        framebuffer_size: np.ndarray
        """
        return np.array(glfw.get_framebuffer_size(self._window), np.uint32)

    @property
    def framebuffer_width(self) -> int:
        """
        Get framebuffer width in pixels

        Returns
        -------
        framebuffer_width: int
        """
        return self.framebuffer_size[0]

    @property
    def framebuffer_height(self) -> int:
        """
        Get framebuffer height in pixels

        Returns
        -------
        framebuffer_height: int
        """
        return self.framebuffer_size[1]

    @property
    def position(self) -> np.ndarray:
        """
        Get Window position (x,y) in screen coordinates

        Returns
        -------
        position: np.ndarray
        """
        return np.array(glfw.get_window_pos(self._window), np.int32)

    @position.setter
    def position(self, value: np.ndarray):
        """
        Set Window position (x,y) in screen coordinates
        Parameters
        ----------
        value: np.ndarray
        """
        glfw.set_window_pos(self._window, value[0], value[1])

    @property
    def title(self) -> str:
        """
        Get Window title

        Returns
        -------
        title: str
        """
        return self._title

    @title.setter
    def title(self, value: str):
        """
        Set Window title

        Parameters
        ----------
        value: str
        """
        self._title = value
        glfw.set_window_title(self._window, value)

    @property
    def vsync(self) -> int:
        """
        Get Vsync

        Returns
        -------
        vsync: int
        """
        return self._vsync

    @vsync.setter
    def vsync(self, value: int):
        """
        Set Vsync

        Parameters
        ----------
        value: int
        """
        glfw.swap_interval(value)
        self._vsync = value

    @property
    def time_update(self) -> float:
        """
        Time on_update took in seconds

        Returns
        -------
        time_update: float
        """
        return self._time_update

    @property
    def time_draw(self) -> float:
        """
        Time on_draw took in seconds

        Returns
        -------
        time_draw: float
        """
        return self._time_draw

    @property
    def time_frame(self) -> float:
        """
        Time frame (= on_update + on_draw + vsync) took in seconds

        Returns
        -------
        time_frame: float
        """
        return self._time_frame

    def close(self):
        """
        Close Window

        When using the context manager (i.e. the 'with' statement):
        this function will be called on the context managers __exit__().
        """
        glfw.set_window_should_close(self._window, True)

        Canvas.COUNT -= 1

        if Canvas.COUNT == 0:
            glfw.terminate()
        
    def iconify(self):
        """Iconify (i.e. Minimize) Window"""
        glfw.iconify_window(self._window)

    def restore(self):
        """Restore Window from iconified state"""
        glfw.restore_window(self._window)

    def maximize(self):
        """Maximize Window"""
        glfw.maximize_window(self._window)

    def show(self):
        """Show hidden Window"""
        glfw.show_window(self._window)

    def hide(self):
        """Hide visible Window"""
        glfw.hide_window(self._window)

    def focus(self):
        """Get Input Focus for this Window"""
        glfw.focus_window(self._window)

    def run(self):
        """Run Window"""
        while not glfw.window_should_close(self._window):
            self.update()
        glfw.destroy_window(self._window)

    def update(self):
        """
        Update Frame:
        1. Call on_update
        2. Call on_draw
        3. Swap Buffers (and wait for Vertical Synchronisation)
        4. Poll Events
        """
        t0 = self._time_last_frame
        t1 = time()
        self._time_last_frame = t1

        self.on_update(t1 - t0)
        self._time_update = time() - t1

        t1 = time()
        self.on_draw()
        self._time_draw = time() - t1

        glfw.swap_buffers(self._window)
        self._event_processing_func()
        self._time_frame = time() - t1

    def on_update(self, dt: float):
        """
        On Update Event

        Parameters
        ----------
        dt: float
            time since last frame in seconds
        """
        pass

    def on_draw(self):
        """On Draw Event"""
        pass

    def on_window_move(self, position: np.ndarray):
        """
        On Window Move Event

        Parameters
        ----------
        position: np.ndarray
            Current Window position (x,y)
        """
        pass

    def on_resize(self, size: np.ndarray):
        """
        On Window Resize Event

        Parameters
        ----------
        size: np.ndarray
            Current Window size (w,h) in pixels
        """
        pass

    def on_close(self):
        """On Window Close Event"""
        pass

    def on_refresh(self):
        """On Window Refresh Event"""
        pass

    def on_focus(self, value: bool):
        """
        On Window Focus (True/False) Event

        Parameters
        ----------
        value: bool
            Whether Window is focused
        """
        pass

    def on_iconify(self, value: bool):
        """
        On Window Iconify (True/False) Event

        Parameters
        ----------
        value: bool
            Whether Window is iconified
        """
        pass

    def on_framebuffer_resize(self, size: np.ndarray):
        """
        On Window Framebuffer Resize Event

        Parameters
        ----------
        size: np.ndarray
            Current Framebuffer size in pixels
        """
        pass

    def on_key(self, key: Key, action: Action, modifier: Modifier):
        """
        On Keyboard Key Press/Release/Hold Event

        Parameters
        ----------
        key: Key
        action: Action
        modifier: Modifier
        """
        pass

    def on_char(self, char: str):
        """
        On Character Event (based on users keyboard layout and language setting)

        Parameters
        ----------
        char: str
        """
        pass

    def on_mouse_move(self, position: np.ndarray):
        """
        On Mouse Move Event

        Parameters
        ----------
        position: np.ndarray
            Mouse Position in Local Screen Coordinates
        """
        pass

    def on_mouse_button(self, button: Button, action: Action, modifier: Modifier):
        """
        On Mouse Button Event

        Parameters
        ----------
        button: Button
        action: Action
        modifier: Modifier
        """
        pass

    def on_scroll(self, offset: np.ndarray):
        """
        On Scroll Event

        Parameters
        ----------
        offset: np.ndarray
        """
        pass

    def _on_move(self, window: glfw.Window, x: int, y: int):
        """
        Raw On Move Event

        Parameters
        ----------
        window: glfw.Window
        x: int
        y: int
        """
        self.on_window_move(np.array([x, y], np.int32))

    def _on_resize(self, window: glfw.Window, width: int, height: int):
        """
        Raw On Resize Event

        Parameters
        ----------
        window: glfw.Window
        width: int
        height: int
        """
        self.on_resize(np.array([width, height], np.int32))

    def _on_close(self, window: glfw.Window):
        """
        Raw On Close Event

        Parameters
        ----------
        window: glfw.Window
        """
        self.on_close()

    def _on_refresh(self, window: glfw.Window):
        """
        Raw On Refresh Event

        Parameters
        ----------
        window: glfw.Window
        """
        self.on_refresh()

    def _on_focus(self, window: glfw.Window, value: int):
        """
        Raw On Focus Event

        Parameters
        ----------
        window: glfw.Window
        value: int
        """
        self.on_focus(bool(value))

    def _on_iconify(self, window: glfw.Window, value: int):
        """
        Raw On Iconify Event

        Parameters
        ----------
        window: glfw.Window
        value: int
        """
        self.on_iconify(bool(value))

    def _on_framebuffer_resize(self, window: glfw.Window, x: int, y: int):
        """
        Raw On Framebuffer Resize Event

        Parameters
        ----------
        window: glfw.Window
        x: int
        y: int
        """
        self.on_framebuffer_resize(np.array([x, y], np.int32))

    def _on_key(self, window: glfw.Window, key: int, scancode: int, action: int, mods: int):
        """
        Raw On Keyboard Key Event

        Parameters
        ----------
        window: glfw.Window
        key: int
        scancode: int
        action: int
        mods: int
        """
        self.on_key(Key(key), Action(action), Modifier(mods))

    def _on_char(self, window: glfw.Window, char: int):
        """
        Raw on Char Event

        Parameters
        ----------
        window: glfw.Window
        char: int
        """
        self.on_char(chr(char))

    def _on_mouse_move(self, window: glfw.Window, x: float, y: float):
        """
        Raw On Mouse Move Event

        Parameters
        ----------
        window: glfw.Window
        x: float
        y: float
        """
        self.on_mouse_move(np.array([x,y], np.float32))

    def _on_mouse_button(self, window: glfw.Window, button: int, action: int, mods: int):
        """
        Raw On Mouse Button Event

        Parameters
        ----------
        window: glfw.Window
        button: int
        action: int
        mods: int
        """
        self.on_mouse_button(Button(button), Action(action), Modifier(mods))

    def _on_scroll(self, window: glfw.Window, x: float, y: float):
        """
        Raw On Scroll Event

        Parameters
        ----------
        window: glfw.Window
        x: float
        y: float
        """
        self.on_scroll(np.array([x,y], np.float32))

    def __enter__(self):
        """
        Context Manager __enter__

        Returns
        -------
        self: Canvas
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context Manager __exit__
        """
        self.close()

    def __str__(self) -> str:
        """
        Canvas string representation <class name> '<title>'

        Returns
        -------
        __str__: str
        """
        return "{} '{}'".format(self.__class__.__name__, self.title)

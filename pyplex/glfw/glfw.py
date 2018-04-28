from ctypes import *
from typing import *
import os


class NotInitializedError(Exception):
    """
    GLFW Not Initialized Error

    This occurs if a GLFW function was called that must not be called unless the library is initialized.

    Application programmer error. Initialize GLFW before calling any function that requires initialization.
    """
    pass


class NoCurrentContextError(Exception):
    """
    GLFW No Current Context Error

    This occurs if a GLFW function was called that needs and operates on the current OpenGL or OpenGL ES context
    but no context is current on the calling thread. One such function is glfwSwapInterval.

    Application programmer error. Ensure a context is current before calling functions that require a current context.
    """
    pass


class InvalidEnumError(Exception):
    """
    GLFW Invalid Enum Error

    One of the arguments to the function was an invalid enum value,
    for example requesting GLFW_RED_BITS with glfwGetWindowAttrib.

    Application programmer error. Fix the offending call.
    """
    pass


class InvalidValueError(Exception):
    """
    GLFW Invalid Value Error

    One of the arguments to the function was an invalid value,
    for example requesting a non-existent OpenGL or OpenGL ES version like 2.7.

    Requesting a valid but unavailable OpenGL or OpenGL ES version will instead result in a
    GLFW_VERSION_UNAVAILABLE error.

    Application programmer error. Fix the offending call.
    """
    pass


class OutOfMemoryError(Exception):
    """
    GLFW Out of Memory Error

    A memory allocation failed.

    A bug in GLFW or the underlying operating system. Report the bug to our issue tracker.
    """
    pass


class APIUnavailableError(Exception):
    """
    GLFW API Unavailable Error

    GLFW could not find support for the requested API on the system.

    The installed graphics driver does not support the requested API, or does not support it via the chosen context
    creation backend. Below are a few examples.

    Some pre-installed Windows graphics drivers do not support OpenGL. AMD only supports OpenGL ES via EGL,
    while Nvidia and Intel only support it via a WGL or GLX extension. OS X does not provide OpenGL ES at all.
    The Mesa EGL, OpenGL and OpenGL ES libraries do not interface with the Nvidia binary driver.
    Older graphics drivers do not support Vulkan.
    """
    pass


class VersionUnavailableError(Exception):
    """
    GLFW Version Unavailable Error

    The requested OpenGL or OpenGL ES version (including any requested context or framebuffer hints)
    is not available on this machine.

    The machine does not support your requirements. If your application is sufficiently flexible,
    downgrade your requirements and try again.
    Otherwise, inform the user that their machine does not match your requirements.

    Future invalid OpenGL and OpenGL ES versions, for example OpenGL 4.8 if 5.0 comes out before the 4.x series gets
    that far, also fail with this error and not GLFW_INVALID_VALUE,
    because GLFW cannot know what future versions will exist.
    """
    pass


class PlatformError(Exception):
    """
    GLFW Platform Error

    A platform-specific error occurred that does not match any of the more specific categories.

    A bug or configuration error in GLFW, the underlying operating system or its drivers, or a lack of required
    resources. Report the issue to our issue tracker.
    """
    pass


class FormatUnavailableError(Exception):
    """
    GLFW Format Unavailable Error

    If emitted during window creation, the requested pixel format is not supported.

    If emitted when querying the clipboard, the contents of the clipboard could not be converted to requested format.

    If emitted during window creation, one or more hard constraints did not match any of the available pixel formats.
    If your application is sufficiently flexible, downgrade your requirements and try again.
    Otherwise, inform the user that their machine does not match your requirements.

    If emitted when querying the clipboard, ignore the error or report it to the user, as appropriate.
    """
    pass


class NoWindowContextError(Exception):
    """
    GLFW No Window Context Error

    A window that does not have an OpenGL or OpenGL ES context was passed to a function that requires it to have one.

    Application programmer error. Fix the offending call.
    """
    pass


class Window(Structure):
    """Opaque GLFW Window object"""
    _fields_ = [("id", c_int)]


class Cursor(Structure):
    """Opaque GLFW Cursor object"""
    _fields_ = [("id", c_int)]


class Image(Structure):
    """GLFW Image Data"""
    _fields_ = [
        ("width", c_int),
        ("height", c_int),
        ("pixels", POINTER(c_ubyte))
    ]


class Monitor(Structure):
    """Opaque GLFW Monitor object"""
    _fields_ = [("id", c_int)]


class VideoMode(Structure):
    """GLFW Video Mode"""
    _fields_ = [
        ('width', c_int),
        ('height', c_int),
        ('red_bits', c_int),
        ('green_bits', c_int),
        ('blue_bits', c_int),
        ('refresh_rate', c_int)
    ]


class GammaRamp(Structure):
    """GLFW Gamma Ramp"""
    _fields_ = [
        ('red', POINTER(c_ushort)),
        ('green', POINTER(c_ushort)),
        ('blue', POINTER(c_ushort)),
        ('size', c_uint)
    ]


class GLFW:

    ERROR_CALLBACK = CFUNCTYPE(None, c_int, c_char_p)

    WINDOW_POSITION_CALLBACK = CFUNCTYPE(None, Window, c_int, c_int)
    WINDOW_SIZE_CALLBACK = CFUNCTYPE(None, Window, c_int, c_int)
    WINDOW_CLOSE_CALLBACK = CFUNCTYPE(None, Window)
    WINDOW_REFRESH_CALLBACK = CFUNCTYPE(None, Window)
    WINDOW_FOCUS_CALLBACK = CFUNCTYPE(None, Window, c_int)
    WINDOW_ICONIFY_CALLBACK = CFUNCTYPE(None, Window, c_int)
    FRAMEBUFFER_SIZE_CALLBACK = CFUNCTYPE(None, Window, c_int, c_int)

    MOUSE_BUTTON_CALLBACK = CFUNCTYPE(None, Window, c_int, c_int, c_int)
    CURSOR_POSITION_CALLBACK = CFUNCTYPE(None, Window, c_double, c_double)
    CURSOR_ENTER_CALLBACK = CFUNCTYPE(None, Window, c_int)
    SCROLL_CALLBACK = CFUNCTYPE(None, Window, c_double, c_double)
    KEY_CALLBACK = CFUNCTYPE(None, Window, c_int, c_int, c_int, c_int)
    CHAR_CALLBACK = CFUNCTYPE(None, Window, c_uint)
    CHAR_MODS_CALLBACK = CFUNCTYPE(None, Window, c_uint, c_int)

    DROP_CALLBACK = CFUNCTYPE(None, Window, c_int, POINTER(c_char_p))

    JOYSTICK_CALLBACK = CFUNCTYPE(None, c_int, c_int)
    MONITOR_CALLBACK = CFUNCTYPE(None, Monitor, c_int)

    _DLL_WIN = os.path.join(os.path.dirname(__file__), 'bin', 'glfw3_x64.dll')

    _ERROR = {
        0x00010001: NotInitializedError,
        0x00010002: NoCurrentContextError,
        0x00010003: InvalidEnumError,
        0x00010004: InvalidValueError,
        0x00010005: OutOfMemoryError,
        0x00010006: APIUnavailableError,
        0x00010007: VersionUnavailableError,
        0x00010008: PlatformError,
        0x00010009: FormatUnavailableError,
        0x000100010: NoWindowContextError,
    }

    def __init__(self):
        """
        GLFW is a free, Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan application development.
        It provides a simple, platform-independent API for creating windows, contexts and surfaces, reading input,
        handling events, etc.

        This class wraps GLFW for use in Python in combination with OpenGL. With this in mind, this wrapper does not
        include Vulkan and native access functionality. All other functions are present.

        This class uses ctypes to do a bare bones wrapping of GLFW, with the following considerations:
            - Functions in style glfwFunctionName() are translated as GLFW.function_name()
            - Direct low level ctypes translation is done for all types/structs encountered in GLFW
            - All functions are documented in Python/Numpy style, with the source being glfw.org
            - GLFW Errors are raised as Python Errors, which can be disabled with GLFW.set_error_callback()
            - Even though Python functions are defined, they're just for documentation and IDE purposes:
                - function calls are directly forwarded to the GLFW implementation, using ctypes for type casting
                    - This is done out of performance considerations, eliminating unnecessary function calls
        """

        self._dll = CDLL(self._DLL_WIN)
        self._wrap_all()
        self.__error_callback = self.ERROR_CALLBACK(self._error_callback)
        self.set_error_callback(self.__error_callback)

    def make_context_current(self, window: Optional[Window]):
        """
        Makes the context of the specified window current for the calling thread.

        This function makes the OpenGL or OpenGL ES context of the specified window current on the calling thread.
        A context can only be made current on a single thread at a time and each thread can have only a single current
        context at a time.

        By default, making a context non-current implicitly forces a pipeline flush. On machines that support
        GL_KHR_context_flush_control, you can control whether a context performs this flush by setting the
        GLFW_CONTEXT_RELEASE_BEHAVIOR window hint.

        The specified window must have an OpenGL or OpenGL ES context. Specifying a window without a context will
        generate a GLFW_NO_WINDOW_CONTEXT error.

        Parameters
        ----------
        window: Window
            The window whose context to make current, or NULL to detach the current context.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_NO_WINDOW_CONTEXT and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_current_context(self) -> Window:
        """
        Returns the window whose context is current on the calling thread.

        Returns
        -------
        window: Window
            The window whose context is current, or NULL if no window's context is current.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def swap_interval(self, interval: int):
        """
        Sets the swap interval for the current context.

        This function sets the swap interval for the current OpenGL or OpenGL ES context,
        i.e. the number of screen updates to wait from the time glfwSwapBuffers was called before swapping the
        buffers and returning. This is sometimes called vertical synchronization, vertical retrace synchronization
        or just vsync.

        Contexts that support either of the WGL_EXT_swap_control_tear and GLX_EXT_swap_control_tear extensions also
        accept negative swap intervals, which allow the driver to swap even if a frame arrives a little bit late.
        You can check for the presence of these extensions using glfwExtensionSupported. For more information about
        swap tearing, see the extension specifications.

        A context must be current on the calling thread. Calling this function without a current context will cause a
        GLFW_NO_CURRENT_CONTEXT error.

        This function does not apply to Vulkan. If you are rendering with Vulkan, see the present mode of your
        swapchain instead.

        Parameters
        ----------
        interval: int
            The minimum number of screen updates to wait for until the buffers are swapped by glfwSwapBuffers.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_NO_CURRENT_CONTEXT and GLFW_PLATFORM_ERROR.

        Notes
        -----
        This function is not called during context creation, leaving the swap interval set to whatever is the default
        on that platform. This is done because some swap interval extensions used by GLFW do not allow the swap
        interval to be reset to zero once it has been set to a non-zero value.

        GPU drivers do not honor the requested swap interval, either because of a user setting that overrides the
        application's request or due to bugs in the driver.
        """
        pass

    def extension_supported(self, extension: bytes) -> c_int:
        """
        Returns whether the specified extension is available.

        This function returns whether the specified API extension is supported by the current OpenGL or OpenGL ES
        context. It searches both for client API extension and context creation API extensions.

        A context must be current on the calling thread. Calling this function without a current context will cause a
        GLFW_NO_CURRENT_CONTEXT error.

        As this functions retrieves and searches one or more extension strings each call, it is recommended that you
        cache its results if it is going to be used frequently. The extension strings will not change during the
        lifetime of a context, so there is no danger in doing this.

        This function does not apply to Vulkan. If you are using Vulkan, see glfwGetRequiredInstanceExtensions,
        vkEnumerateInstanceExtensionProperties and vkEnumerateDeviceExtensionProperties instead.

        Parameters
        ----------
        extension: c_char_p
            The ASCII encoded name of the extension.

        Returns
        -------
        GLFW_TRUE if the extension is available, or GLFW_FALSE otherwise.

        Raises
        ------
        Possible errors: GLFW_NOT_INITIALIZED, GLFW_NO_CURRENT_CONTEXT, GLFW_INVALID_VALUE and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_proc_address(self, procname: bytes) -> c_void_p:
        """
        Returns the address of the specified function for the current context.

        This function returns the address of the specified OpenGL or OpenGL ES core or extension function,
        if it is supported by the current context.

        A context must be current on the calling thread. Calling this function without a current context will cause a
        GLFW_NO_CURRENT_CONTEXT error.

        This function does not apply to Vulkan. If you are rendering with Vulkan, see glfwGetInstanceProcAddress,
        vkGetInstanceProcAddr and vkGetDeviceProcAddr instead.

        Parameters
        ----------
        procname: c_char_p
            The ASCII encoded name of the function.

        Returns
        -------
        The address of the function, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_NO_CURRENT_CONTEXT and GLFW_PLATFORM_ERROR.

        Notes
        -----
        The address of a given function is not guaranteed to be the same between contexts.
        This function may return a non-NULL address despite the associated version or extension not being available.
        Always check the context version or extension string first.
        """
        pass

    def init(self) -> int:
        """
        Initializes the GLFW library.

        This function initializes the GLFW library. Before most GLFW functions can be used, GLFW must be initialized,
        and before an application terminates GLFW should be terminated in order to free any resources allocated during
        or after initialization.

        If this function fails, it calls glfwTerminate before returning. If it succeeds, you should call glfwTerminate
        before the application exits.

        Additional calls to this function after successful initialization but before termination will return GLFW_TRUE
        immediately.

        Returns
        -------
        GLFW_TRUE if successful, or GLFW_FALSE if an error occurred.

        Raises
        ------
        Possible errors include GLFW_PLATFORM_ERROR.
        """
        pass

    def terminate(self):
        """
        Terminates the GLFW library.

        This function destroys all remaining windows and cursors, restores any modified gamma ramps and frees any other
        allocated resources. Once this function is called, you must again call glfwInit successfully before you will
        be able to use most GLFW functions.

        If GLFW has been successfully initialized, this function should be called before the application exits.
        If initialization fails, there is no need to call this function, as it is called by glfwInit before it returns
        failure.

        Raises
        ------
        Possible errors include GLFW_PLATFORM_ERROR.
        """
        pass

    def get_version(self, major: POINTER(c_int), minor: POINTER(c_int), rev: POINTER(c_int)):
        """
        Retrieves the version of the GLFW library.

        This function retrieves the major, minor and revision numbers of the GLFW library.
        It is intended for when you are using GLFW as a shared library and want to ensure that you are using the
        minimum required version.

        Any or all of the version arguments may be NULL.

        Parameters
        ----------
        major: POINTER(c_int)
            Where to store the major version number, or NULL.
        minor: POINTER(c_int)
            Where to store the minor version number, or NULL.
        rev: POINTER(c_int)
            Where to store the revision number, or NULL.
        """
        pass

    def get_version_string(self) -> c_char_p:
        """
        Returns a string describing the compile-time configuration.

        This function returns the compile-time generated version string of the GLFW library binary.
        It describes the version, platform, compiler and any platform-specific compile-time options.
        It should not be confused with the OpenGL or OpenGL ES version string, queried with glGetString.

        Do not use the version string to parse the GLFW library version. The glfwGetVersion function provides the
        version of the running library binary in numerical format.

        Returns
        -------
        version: c_char_p
            The ASCII encoded GLFW version string.

        Notes
        -----
        This function may be called before glfwInit.
        """
        pass

    def set_error_callback(self, cbfun: ERROR_CALLBACK) -> ERROR_CALLBACK:
        """
        Sets the error callback.

        This function sets the error callback, which is called with an error code and a human-readable description each
        time a GLFW error occurs.

        The error callback is called on the thread where the error occurred. If you are using GLFW from multiple
        threads, your error callback needs to be written accordingly.

        Because the description string may have been generated specifically for that error, it is not guaranteed to be
        valid after the callback has returned. If you wish to use it after the callback returns,
        you need to make a copy.

        Once set, the error callback remains set even after the library has been terminated.

        Returns
        -------
        callback: ERROR_CALLBACK_TYPE
            The previously set callback, or NULL if no callback was set.
        """
        pass

    def default_window_hints(self):
        """
        Resets all window hints to their default values.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def window_hint(self, hint: int, value: int):
        """
        Sets the specified window hint to the desired value.

        This function sets hints for the next call to glfwCreateWindow. The hints, once set, retain their values until
        changed by a call to glfwWindowHint or glfwDefaultWindowHints, or until the library is terminated.

        This function does not check whether the specified hint values are valid.
        If you set hints to invalid values this will instead be reported by the next call to glfwCreateWindow.

        Parameters
        ----------
        hint: int
            The window hint to set.
        value: int
            The new value of the window hint.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_INVALID_ENUM.
        """
        pass

    def create_window(self, width: int, height: int, title: bytes,
                      monitor: Optional[Monitor], share: Optional[Window]):
        """
        Creates a window and its associated context.

        This function creates a window and its associated OpenGL or OpenGL ES context. Most of the options controlling
        how the window and its context should be created are specified with window hints.

        Successful creation does not change which context is current. Before you can use the newly created context,
        you need to make it current. For information about the share parameter, see Context object sharing.

        The created window, framebuffer and context may differ from what you requested, as not all parameters and hints
        are hard constraints. This includes the size of the window, especially for full screen windows. To query the
        actual attributes of the created window, framebuffer and context, see glfwGetWindowAttrib, glfwGetWindowSize
        and glfwGetFramebufferSize.

        To create a full screen window, you need to specify the monitor the window will cover. If no monitor is
        specified, the window will be windowed mode. Unless you have a way for the user to choose a specific monitor,
        it is recommended that you pick the primary monitor. For more information on how to query connected monitors,
        see Retrieving monitors.

        For full screen windows, the specified size becomes the resolution of the window's desired video mode. As long
        as a full screen window is not iconified, the supported video mode most closely matching the desired video mode
        is set for the specified monitor. For more information about full screen windows, including the creation of so
        called windowed full screen or borderless full screen windows, see "Windowed full screen" windows.

        Once you have created the window, you can switch it between windowed and full screen mode with
        glfwSetWindowMonitor. If the window has an OpenGL or OpenGL ES context, it will be unaffected.

        By default, newly created windows use the placement recommended by the window system. To create the window at
        a specific position, make it initially invisible using the GLFW_VISIBLE window hint, set its position and then
        show it.

        As long as at least one full screen window is not iconified, the screensaver is prohibited from starting.

        Window systems put limits on window sizes. Very large or very small window dimensions may be overridden by the
        window system on creation. Check the actual size after creation.

        The swap interval is not set during window creation and the initial value may vary depending on driver settings
        and defaults.

        Parameters
        ----------
        width: int
            The desired width, in screen coordinates, of the window. This must be greater than zero.
        height: int
            The desired height, in screen coordinates, of the window. This must be greater than zero.
        title: bytes
            The initial, UTF-8 encoded window title.
        monitor: Monitor
            The monitor to use for full screen mode, or NULL for windowed mode.
        share: Window
            The window whose context to share resources with, or NULL to not share resources.

        Returns
        -------
        window: Window
            The handle of the created window, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM, GLFW_INVALID_VALUE, GLFW_API_UNAVAILABLE,
        GLFW_VERSION_UNAVAILABLE, GLFW_FORMAT_UNAVAILABLE and GLFW_PLATFORM_ERROR.

        Notes
        -----
        Windows: Window creation will fail if the Microsoft GDI software OpenGL implementation is the only one
        available.

        Windows: If the executable has an icon resource named GLFW_ICON, it will be set as the initial icon for the
        window. If no such icon is present, the IDI_WINLOGO icon will be used instead. To set a different icon, see
        glfwSetWindowIcon.

        Windows: The context to share resources with must not be current on any other thread.

        OS X: The GLFW window has no icon, as it is not a document window, but the dock icon will be the same as the
        application bundle's icon. For more information on bundles, see the Bundle Programming Guide in the Mac
        Developer Library.

        OS X: The first time a window is created the menu bar is populated with common commands like Hide, Quit and
        About. The About entry opens a minimal about dialog with information from the application's bundle. The menu
        bar can be disabled with a compile-time option.

        OS X: On OS X 10.10 and later the window frame will not be rendered at full resolution on Retina displays
        unless the NSHighResolutionCapable key is enabled in the application bundle's Info.plist. For more information,
        see High Resolution Guidelines for OS X in the Mac Developer Library. The GLFW test and example programs use a
        custom Info.plist template for this, which can be found as CMake/MacOSXBundleInfo.plist.in in the source tree.

        X11: Some window managers will not respect the placement of initially hidden windows.

        X11: Due to the asynchronous nature of X11, it may take a moment for a window to reach its requested state.
        This means you may not be able to query the final size, position or other attributes directly after window
        creation.
        """
        pass

    def destroy_window(self, window: Window):
        """
        Destroys the specified window and its context.

        This function destroys the specified window and its context. On calling this function, no further callbacks
        will be called for that window.

        If the context of the specified window is current on the main thread, it is detached before being destroyed.

        Parameters
        ----------
        window: Window
            The window to destroy.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def window_should_close(self, window: Window) -> int:
        """
        Checks the close flag of the specified window.

        This function returns the value of the close flag of the specified window.

        Parameters
        ----------
        window: Window
            The window to query.

        Returns
        -------
        flag: int
            The value of the close flag.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_window_should_close(self, window: Window, value: int):
        """
        Sets the close flag of the specified window.

        This function sets the value of the close flag of the specified window.
        This can be used to override the user's attempt to close the window, or to signal that it should be closed.

        Parameters
        ----------
        window: Window
            The window whose flag to change.
        value: int
            The new value.

        Raises
        -------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_window_title(self, window: Window, title: bytes):
        """
        Sets the title of the specified window.

        This function sets the window title, encoded as UTF-8, of the specified window.

        Parameters
        ----------
        window: Window
            The window whose title to change.
        title: bytes
            The UTF-8 encoded window title.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.

        Notes
        -----
        OS X: The window title will not be updated until the next time you process events.
        """
        pass

    def set_window_icon(self, window: Window, count: int, images: Image):
        """
        TODO: Fix For Multiple Images!

        Sets the icon for the specified window.

        This function sets the icon of the specified window. If passed an array of candidate images,
        those of or closest to the sizes desired by the system are selected. If no images are specified,
        the window reverts to its default icon.

        The desired image sizes varies depending on platform and system settings.
        The selected images will be rescaled as needed. Good sizes include 16x16, 32x32 and 48x48.

        Parameters
        ----------
        window: Window
            The window whose icon to set.
        count: int
            The number of images in the specified array, or zero to revert to the default window icon.
        images: Image
            The images to create the icon from. This is ignored if count is zero.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.

        -----
        OS X: The GLFW window has no icon, as it is not a document window, so this function does nothing.
        The dock icon will be the same as the application bundle's icon. For more information on bundles,
        see the Bundle Programming Guide in the Mac Developer Library.

        """

        pass

    def get_window_pos(self, window: Window, xpos: POINTER(c_int), ypos: POINTER(c_int)):
        """
        Retrieves the position of the client area of the specified window.

        This function retrieves the position, in screen coordinates, of the upper-left corner of the client area of
        the specified window.

        Any or all of the position arguments may be NULL.
        If an error occurs, all non-NULL position arguments will be set to zero.

        Parameters
        ----------
        window: Window
            The window to query.
        xpos: POINTER(c_int)
            Where to store the x-coordinate of the upper-left corner of the client area, or NULL.
        ypos: POINTER(c_int)
            Where to store the y-coordinate of the upper-left corner of the client area, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_window_pos(self, window: Window, xpos: int, ypos: int):
        """
        Sets the position of the client area of the specified window.

        This function sets the position, in screen coordinates, of the upper-left corner of the client area of the
        specified windowed mode window. If the window is a full screen window, this function does nothing.

        Do not use this function to move an already visible window unless you have very good reasons for doing so,
        as it will confuse and annoy the user.

        The window manager may put limits on what positions are allowed.
        GLFW cannot and should not override these limits.

        Parameters
        ----------
        window: Window
            The window to query.
        xpos: int
            The x-coordinate of the upper-left corner of the client area.
        ypos: int
            The y-coordinate of the upper-left corner of the client area.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_window_size(self, window: Window, width: POINTER(c_int), height: POINTER(c_int)):
        """
        Retrieves the size of the client area of the specified window.

        This function retrieves the size, in screen coordinates, of the client area of the specified window.
        If you wish to retrieve the size of the framebuffer of the window in pixels, see glfwGetFramebufferSize.

        Any or all of the size arguments may be NULL.
        If an error occurs, all non-NULL size arguments will be set to zero.

        Parameters
        ----------
        window: Window
            The window whose size to retrieve.
        width: POINTER(c_int)
            Where to store the width, in screen coordinates, of the client area, or NULL.
        height: POINTER(c_int)
            Where to store the height, in screen coordinates, of the client area, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_window_size_limits(self, window: Window, min_width: int, min_height: int, max_width: int, max_height: int):
        """
        Sets the size limits of the specified window.

        This function sets the size limits of the client area of the specified window.
        If the window is full screen, the size limits only take effect once it is made windowed.
        If the window is not resizable, this function does nothing.

        The size limits are applied immediately to a windowed mode window and may cause it to be resized.

        The maximum dimensions must be greater than or equal to the minimum dimensions and all
        must be greater than or equal to zero.

        Parameters
        ----------
        window: Window
            The window to set limits for.
        min_width: int
            The minimum width, in screen coordinates, of the client area, or GLFW_DONT_CARE.
        min_height: int
            The minimum height, in screen coordinates, of the client area, or GLFW_DONT_CARE.
        max_width: int
            The maximum width, in screen coordinates, of the client area, or GLFW_DONT_CARE.
        max_height: int
            The maximum height, in screen coordinates, of the client area, or GLFW_DONT_CARE.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_VALUE and GLFW_PLATFORM_ERROR.

        Notes
        -----
        If you set size limits and an aspect ratio that conflict, the results are undefined.
        """
        pass

    def set_window_aspect_ratio(self, window: Window, numerator: int, denominator: int):
        """
        Sets the aspect ratio of the specified window.

        This function sets the required aspect ratio of the client area of the specified window.
        If the window is full screen, the aspect ratio only takes effect once it is made windowed.
        If the window is not resizable, this function does nothing.

        The aspect ratio is specified as a numerator and a denominator and both values must be greater than zero.
        For example, the common 16:9 aspect ratio is specified as 16 and 9, respectively.

        If the numerator and denominator is set to GLFW_DONT_CARE then the aspect ratio limit is disabled.

        The aspect ratio is applied immediately to a windowed mode window and may cause it to be resized.

        Parameters
        ----------
        window: Window
            The window to set limits for.
        numerator: int
            The numerator of the desired aspect ratio, or GLFW_DONT_CARE.
        denominator: int
            The denominator of the desired aspect ratio, or GLFW_DONT_CARE.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_VALUE and GLFW_PLATFORM_ERROR.

        Notes
        -----
        If you set size limits and an aspect ratio that conflict, the results are undefined.
        """
        pass

    def set_window_size(self, window: Window, width: int, height: int):
        """
        Sets the size of the client area of the specified window.

        This function sets the size, in screen coordinates, of the client area of the specified window.

        For full screen windows, this function updates the resolution of its desired video mode and switches to the
        video mode closest to it, without affecting the window's context. As the context is unaffected,
        the bit depths of the framebuffer remain unchanged.

        If you wish to update the refresh rate of the desired video mode in addition to its resolution,
        see glfwSetWindowMonitor.

        The window manager may put limits on what sizes are allowed. GLFW cannot and should not override these limits.

        Parameters
        ----------
        window: Window
            The window to resize.
        width: int
            The desired width, in screen coordinates, of the window client area.
        height: int
            The desired height, in screen coordinates, of the window client area.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_framebuffer_size(self, window: Window, width: POINTER(c_int), height: POINTER(c_int)):
        """
        Retrieves the size of the framebuffer of the specified window.

        This function retrieves the size, in pixels, of the framebuffer of the specified window. If you wish to
        retrieve the size of the window in screen coordinates, see glfwGetWindowSize.

        Any or all of the size arguments may be NULL.
        If an error occurs, all non-NULL size arguments will be set to zero.

        Parameters
        ----------
        window: Window
            The window whose framebuffer to query.
        width: POINTER(c_int)
            Where to store the width, in pixels, of the framebuffer, or NULL.
        height: POINTER(c_int)
            Where to store the height, in pixels, of the framebuffer, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_window_frame_size(self, window: Window, left: POINTER(c_int), top: POINTER(c_int),
                              right: POINTER(c_int), bottom: POINTER(c_int)):
        """
        Retrieves the size of the frame of the window.

        This function retrieves the size, in screen coordinates, of each edge of the frame of the specified window.
        This size includes the title bar, if the window has one. The size of the frame may vary depending on the
        window-related hints used to create it.

        Because this function retrieves the size of each window frame edge and not the offset along a particular
        coordinate axis, the retrieved values will always be zero or positive.

        Any or all of the size arguments may be NULL.
        If an error occurs,all non-NULL size arguments will beset to zero.

        Parameters
        ----------
        window: Window
            The window whose frame size to query.
        left: POINTER(c_int)
            Where to store the size, in screen coordinates, of the left edge of the window frame, or NULL.
        top: POINTER(c_int)
            Where to store the size, in screen coordinates, of the top edge of the window frame, or NULL.
        right: POINTER(c_int)
            Where to store the size, in screen coordinates, of the right edge of the window frame, or NULL.
        bottom: POINTER(c_int)
            Where to store the size, in screen coordinates, of the bottom edge of the window frame, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def iconify_window(self, window: Window):
        """
        Iconifies the specified window.

        This function iconifies (minimizes) the specified window if it was previously restored.
        If the window is already iconified, this function does nothing.

        If the specified window is a full screen window,
        the original monitor resolution is restored until thewindow is restored.

        Parameters
        ----------
        window: Window
            The window to iconify.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def restore_window(self, window: Window):
        """
        Restores the specified window.

        This function restores the specified window if it was previously iconified (minimized) or maximized.
        If the window is already restored, this function does nothing.

        If the specified window is a full screen window,
        the resolution chosen for the window is restored on the selected monitor.

        Parameters
        ----------
        window: Window
            The window to restore.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def maximize_window(self, window: Window):
        """
        Maximizes the specified window.

        This function maximizes the specified window if it was previously not maximized.
        If the window is already maximized, this function does nothing.

        If the specified window is a full screen window, this function does nothing.

        Parameters
        ----------
        window: Window

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def show_window(self, window: Window):
        """
        Makes the specified window visible.

        This function makes the specified window visible if it was previously hidden.
        If the window is already visible or is in full screen mode, this function does nothing.

        Parameters
        ----------
        window: Window
            The window to make visible.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def hide_window(self, window: Window):
        """
        Hides the specified window.

        This function hides the specified window if it was previously visible.
        If the window is already hidden or is in full screen mode, this function does nothing.

        Parameters
        ----------
        window: Window
            The window to hide.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.

        """
        pass

    def focus_window(self, window: Window):
        """
        Brings the specified window to front and sets input focus.

        This function brings the specified window to front and sets input focus. The window should already be visible
        and not iconified.

        By default, both windowed and full screen mode windows are focused when initially created. Set the GLFW_FOCUSED
        to disable this behavior.

        Do not use this function to steal focus from other applications unless you are certain that is what the user
        wants. Focus stealing can be extremely disruptive.

        Parameters
        ----------
        window: Window
            The window to give input focus.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_window_monitor(self, window: Window) -> Monitor:
        """
        Returns the monitor that the window uses for full screen mode

        This function returns the handle of the monitor that the specified window is in full screen on.

        Parameters
        ----------
        window: Window
            The window to query.

        Returns
        -------
        monitor: Monitor
            The monitor, or NULL if the window is in windowed mode or an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_window_monitor(self, window: Window, monitor: Monitor, xpos: int, ypos: int, width: int, height: int,
                           refresh_rate: int):
        """
        Sets the mode, monitor, video mode and placement of a window.

        This function sets the monitor that the window uses for full screen mode or,
        if the monitor is NULL, makes it windowed mode.

        When setting a monitor, this function updates the width, height and refresh rate of the desired video mode
        and switches to the video mode closest to it. The window position is ignored when setting a monitor.

        When the monitor is NULL, the position, width and height are used to place the window client area.
        The refresh rate is ignored when no monitor is specified.

        If you only wish to update the resolution of a full screen window or the size of a windowed mode window,
        see glfwSetWindowSize.

        When a window transitions from full screen to windowed mode,
        this function restores any previous window settings such as whether it is
        decorated, floating, resizable, has size or aspect ratio limits, etc..

        Parameters
        ----------
        window: Window
            The window whose monitor, size or video mode to set.
        monitor: Monitor
            The desired monitor, or NULL to set windowed mode.
        xpos: int
            The desired x-coordinate of the upper-left corner of the client area.
        ypos: int
            The desired y-coordinate of the upper-left corner of the client area.
        width: int
            The desired with, in screen coordinates, of the client area or video mode.
        height: int
            The desired height, in screen coordinates, of the client area or video mode.
        refresh_rate: int
            The desired refresh rate, in Hz, of the video mode, or GLFW_DONT_CARE.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_window_attribute(self, window: Window, attribute: int) -> int:
        """
        Returns an attribute of the specified window.

        This function returns the value of an attribute of the specified window or its OpenGL or OpenGL ES context.

        Parameters
        ----------
        window: Window
            The window to query.
        attribute: int
            The window attribute whose value to return.

        Returns
        -------
        attribute: int
            The value of the attribute, or zero if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.

        Notes
        -----
        Framebuffer related hints are not window attributes. See Framebuffer related attributes for more information.

        Zero is a valid value for many window and context related attributes so you cannot use a return value of zero
        as an indication of errors. However, this function should not fail as long as it is passed valid arguments
        and the library has been initialized.
        """
        pass

    def set_window_user_pointer(self, window: Window, ptr: c_void_p):
        """
        Sets the user pointer of the specified window.

        This function sets the user-defined pointer of the specified window.
        The current value is retained until the window is destroyed. The initial value is NULL.

        Parameters
        ----------
        window: Window
            The window whose pointer to set.
        ptr: c_void_p
            The new value.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def get_window_user_pointer(self, window: Window) -> c_void_p:
        """
        Returns the user pointer of the specified window.

        This function returns the current value of the user-defined pointer of the specified window.
        The initial value is NULL.

        Parameters
        ----------
        window: Window
            The window whose pointer to return.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.

        """
        pass

    def set_window_pos_callback(self, window: Window, cbfun: WINDOW_POSITION_CALLBACK) -> WINDOW_POSITION_CALLBACK:
        """
        Sets the position callback for the specified window.

        This function sets the position callback of the specified window, which is called when the window is moved.
        The callback is provided with the screen position of the upper-left corner of the client area of the window.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_POSITION_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_POSITION_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        """
        pass

    def set_window_size_callback(self, window: Window, cbfun: WINDOW_SIZE_CALLBACK) -> WINDOW_SIZE_CALLBACK:
        """
        Sets the size callback for the specified window.

        This function sets the size callback of the specified window, which is called when the window is resized.
        The callback is provided with the size, in screen coordinates, of the client area of the window.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_SIZE_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_SIZE_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.
        """
        pass

    def set_window_close_callback(self, window: Window, cbfun: WINDOW_CLOSE_CALLBACK) -> WINDOW_CLOSE_CALLBACK:
        """
        Sets the close callback for the specified window.

        This function sets the close callback of the specified window,
        which is called when the user attempts to close the window,
        for example by clicking the close widget in the title bar.

        The close flag is set before this callback is called,
        but you can modify it at any time with glfwSetWindowShouldClose.

        The close callback is not triggered by glfwDestroyWindow.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_CLOSE_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_CLOSE_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.

        Notes
        -----
        OS X: Selecting Quit from the application menu will trigger the close callback for all windows.
        """
        pass

    def set_window_refresh_callback(self, window: Window, cbfun: WINDOW_REFRESH_CALLBACK) -> WINDOW_REFRESH_CALLBACK:
        """
        Sets the refresh callback for the specified window.

        This function sets the refresh callback of the specified window,
        which is called when the client area of the window needs to be redrawn,
        for example if the window has been exposed after having been covered by another window.

        On compositing window systems such as Aero, Compiz or Aqua, where the window contents are saved off-screen,
        this callback may be called only very infrequently or never at all.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_REFRESH_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_REFRESH_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.
        """
        pass

    def set_window_focus_callback(self, window: Window, cbfun: WINDOW_FOCUS_CALLBACK) -> WINDOW_FOCUS_CALLBACK:
        """
        Sets the focus callback for the specified window.

        This function sets the focus callback of the specified window,
        which is called when the window gains or loses input focus.

        After the focus callback is called for a window that lost input focus,
        synthetic key and mouse button release events will be generated for all such that had been pressed.
        For more information, see glfwSetKeyCallback and glfwSetMouseButtonCallback.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_FOCUS_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_FOCUS_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_window_iconify_callback(self, window: Window, cbfun: WINDOW_ICONIFY_CALLBACK) -> WINDOW_ICONIFY_CALLBACK:
        """
        Sets the iconify callback for the specified window.

        This function sets the iconification callback of the specified window,
        which is called when the window is iconified or restored.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_ICONIFY_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_ICONIFY_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.
        """
        pass

    def set_framebuffer_size_callback(self, window: Window, cbfun: FRAMEBUFFER_SIZE_CALLBACK) -> \
            FRAMEBUFFER_SIZE_CALLBACK:
        """
        Sets the framebuffer resize callback for the specified window.

        This function sets the framebuffer resize callback of the specified window,
        which is called when the framebuffer of the specified window is resized.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: WINDOW_FRAMEBUFFER_SIZE_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        callback: WINDOW_FRAMEBUFFER_SIZE_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def poll_events(self):
        """
        Processes all pending events.

        This function processes only those events that are already in the event queue and then returns immediately.
        Processing events will cause the window and input callbacks associated with those events to be called.

        On some platforms, a window move, resize or menu operation will cause event processing to block. This is due
        to how event processing is designed on those platforms. You can use the window refresh callback to redraw the
        contents of your window when necessary during such operations.

        On some platforms, certain events are sent directly to the application without going through the event queue,
        causing callbacks to be called outside of a call to one of the event processing functions.

        Event processing is not required for joystick input to work.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def wait_events(self):
        """
        Waits until events are queued and processes them.

        This function puts the calling thread to sleep until at least one event is available in the event queue.
        Once one or more events are available, it behaves exactly like glfwPollEvents,
        i.e. the events in the queue are processed and the function then returns immediately.
        Processing events will cause the window and input callbacks associated with those events to be called.

        Since not all events are associated with callbacks, this function may return without a callback having
        been called even if you are monitoring all callbacks.

        On some platforms, a window move, resize or menu operation will cause event processing to block.
        This is due to how event processing is designed on those platforms. You can use the window refresh callback
        to redraw the contents of your window when necessary during such operations.

        On some platforms, certain callbacks may be called outside of a call to one of the event processing functions.

        If no windows exist, this function returns immediately. For synchronization of threads in applications that do
        not create windows, use your threading library of choice.

        Event processing is not required for joystick input to work.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def wait_events_timeout(self, timeout: float):
        """
        Waits with timeout until events are queued and processes them.

        This function puts the calling thread to sleep until at least one event is available in the event queue,
        or until the specified timeout is reached. If one or more events are available,
        it behaves exactly like glfwPollEvents, i.e. the events in the queue are processed and the function then
        returns immediately. Processing events will cause the window and input callbacks associated with those
        events to be called.

        The timeout value must be a positive finite number.

        Since not all events are associated with callbacks, this function may return without a callback having been
        called even if you are monitoring all callbacks.

        On some platforms, a window move, resize or menu operation will cause event processing to block.
        This is due to how event processing is designed on those platforms. You can use the window refresh
        callback to redraw the contents of your window when necessary during such operations.

        On some platforms, certain callbacks may be called outside of a call to one of the event processing functions.

        If no windows exist, this function returns immediately.For synchronization of threads in applications that do
        not create windows, use your threading library of choice.

        Event processing is not required for joystick input to work.

        Parameters
        ----------
        timeout: float
            The maximum amount of time, in seconds, to wait.
        """
        pass

    def post_empty_event(self):
        """
        Posts an empty event to the event queue.

        This function posts an empty event from the current thread to the event queue, causing glfwWaitEvents or
        glfwWaitEventsTimeout to return.

        If no windows exist, this function returns immediately. For synchronization of threads in applications that
        do not create windows, use your threading library of choice.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def swap_buffers(self, window: Window):
        """
        Swaps the front and back buffers of the specified window.

        This function swaps the front and back buffers of the specified window when rendering with OpenGL or OpenGL ES.
        If the swap interval is greater than zero, the GPU driver waits the specified number of screen updates before
        swapping the buffers.

        The specified window must have an OpenGL or OpenGL ES context.
        Specifying a window without a context will generate a GLFW_NO_WINDOW_CONTEXT error.

        This function does not apply to Vulkan. If you are rendering with Vulkan, see vkQueuePresentKHR instead.

        Parameters
        ----------
        window: Window
            The window whose buffers to swap.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_NO_WINDOW_CONTEXT and GLFW_PLATFORM_ERROR.

        Notes
        -----
        EGL: The context of the specified window must be current on the calling thread.
        """
        pass

    def get_input_mode(self, window: Window, mode: int) -> int:
        """
        Returns the value of an input option for the specified window.

        This function returns the value of an input option for the specified window.
        The mode must be one of GLFW_CURSOR, GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.

        Parameters
        ----------
        window: Window
            The window to query.
        mode: int
            One of GLFW_CURSOR, GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_INVALID_ENUM.
        """
        pass

    def set_input_mode(self, window: Window, mode: int, value: int):
        """
        Sets an input option for the specified window.

        This function sets an input mode option for the specified window. The mode must be one of GLFW_CURSOR,
        GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.

        If the mode is GLFW_CURSOR, the value must be one of the following cursor modes:
            GLFW_CURSOR_NORMAL makes the cursor visible and behaving normally.
            GLFW_CURSOR_HIDDEN makes the cursor invisible when it is over the client area of the window but
                does not restrict the cursor from leaving.
            GLFW_CURSOR_DISABLED hides and grabs the cursor, providing virtual and unlimited cursor movement.
                This is useful for implementing for example 3D camera controls.

            If the mode is GLFW_STICKY_KEYS, the value must be either GLFW_TRUE to enable sticky keys, or GLFW_FALSE to
            disable it. If sticky keys are enabled, a key press will ensure that glfwGetKey returns GLFW_PRESS the next
            time it is called even if the key had been released before the call. This is useful when you are only
            interested in whether keys have been pressed but not when or in which order.

            If the mode is GLFW_STICKY_MOUSE_BUTTONS, the value must be either GLFW_TRUE to enable sticky mouse buttons,
            or GLFW_FALSE to disable it. If sticky mouse buttons are enabled, a mouse button press will ensure that
            glfwGetMouseButton returns GLFW_PRESS the next time it is called even if the mouse button had been released
            before the call. This is useful when you are only interested in whether mouse buttons have been pressed but
            not when or in which order.

            Parameters
            ----------
            window: Window
                The window whose input mode to set.
            mode: int
                One of GLFW_CURSOR, GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.
            value: int
                The new value of the specified input mode.

            Raises
            ------
            Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_key_name(self, key: int, scancode: int) -> bytes:
        """
        Returns the localized name of the specified printable key.

        This function returns the localized name of the specified printable key.
        This is intended for displaying key bindings to the user.

        If the key is GLFW_KEY_UNKNOWN, the scancode is used instead, otherwise the scancode is ignored.
        If a non-printable key or (if the key is GLFW_KEY_UNKNOWN) a scancode that maps to a non-printable key is
        specified, this function returns NULL.

        This behavior allows you to pass in the arguments passed to the key callback without modification.

        The printable keys are:
            GLFW_KEY_APOSTROPHE
            GLFW_KEY_COMMA
            GLFW_KEY_MINUS
            GLFW_KEY_PERIOD
            GLFW_KEY_SLASH
            GLFW_KEY_SEMICOLON
            GLFW_KEY_EQUAL
            GLFW_KEY_LEFT_BRACKET
            GLFW_KEY_RIGHT_BRACKET
            GLFW_KEY_BACKSLASH
            GLFW_KEY_WORLD_1
            GLFW_KEY_WORLD_2
            GLFW_KEY_0 to GLFW_KEY_9
            GLFW_KEY_A to GLFW_KEY_Z
            GLFW_KEY_KP_0 to GLFW_KEY_KP_9
            GLFW_KEY_KP_DECIMAL
            GLFW_KEY_KP_DIVIDE
            GLFW_KEY_KP_MULTIPLY
            GLFW_KEY_KP_SUBTRACT
            GLFW_KEY_KP_ADD
            GLFW_KEY_KP_EQUAL

        Parameters
        ----------
        key: int
            The key to query, or GLFW_KEY_UNKNOWN.
        scancode: int
            The scancode of the key to query.

        Returns
        -------
        The localized name of the key, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_key(self, window: Window, key: int) -> int:
        """
        Returns the last reported state of a keyboard key for the specified window.

        This function returns the last state reported for the specified key to the specified window.
        The returned state is one of GLFW_PRESS or GLFW_RELEASE.
        The higher-level action GLFW_REPEAT is only reported to the key callback.

        If the GLFW_STICKY_KEYS input mode is enabled, this function returns GLFW_PRESS the first time you call it for
        a key that was pressed, even if that key has already been released.

        The key functions deal with physical keys, with key tokens named after their use on the standard
        US keyboard layout. If you want to input text, use the Unicode character callback instead.

        The modifier key bit masks are not key tokens and cannot be used with this function.

        Do not use this function to implement text input.

        Parameters
        ----------
        window: Window
            The desired window
        key: int
            The desired keyboard key. GLFW_KEY_UNKNOWN is not a valid key for this function.

        Returns
        -------
        One of GLFW_PRESS or GLFW_RELEASE.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_INVALID_ENUM.
        """
        pass

    def get_mouse_button(self, window: Window, button: int) -> int:
        """
        Returns the last reported state of a mouse button for the specified window.

        This function returns the last state reported for the specified mouse button to the specified window.
        The returned state is one of GLFW_PRESS or GLFW_RELEASE.

        If the GLFW_STICKY_MOUSE_BUTTONS input mode is enabled,
        this function GLFW_PRESS the first time you call it for a mouse button that was pressed,
        even if that mouse button has already been released.

        Parameters
        ----------
        window: Window
            The desired window
        button: int
            The desired mouse button

        Returns
        -------
        One of GLFW_PRESS or GLFW_RELEASE.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_INVALID_ENUM.
        """
        pass

    def get_cursor_pos(self, window: Window, xpos: POINTER(c_double), ypos: POINTER(c_double)):
        """
        Retrieves the position of the cursor relative to the client area of the window.

        This function returns the position of the cursor, in screen coordinates, relative to the upper-left corner of
        the client area of the specified window.

        If the cursor is disabled (with GLFW_CURSOR_DISABLED) then the cursor position is unbounded and limited only by
        the minimum and maximum values of a double.

        The coordinate can be converted to their integer equivalents with the floor function.
        Casting directly to an integer type works for positive coordinates, but fails for negative ones.

        Any or all of the position arguments may be NULL.
        If an error occurs, all non-NULL position arguments will be set to zero.

        Parameters
        ----------
        window: Window
            The desired window.
        xpos: POINTER(c_double)
            Where to store the cursor x-coordinate, relative to the left edge of the client area, or NULL.
        ypos: POINTER(c_double)
            Where to store the cursor y-coordinate, relative to the to top edge of the client area, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.

        """
        pass

    def set_cursor_pos(self, window: Window, xpos: float, ypos: float):
        """
        Sets the position of the cursor, relative to the client area of the window.

        This function sets the position, in screen coordinates, of the cursor relative to the upper-left corner of the
        client area of the specified window. The window must have input focus. If the window does not have input focus
        when this function is called, it fails silently.

        Do not use this function to implement things like camera controls. GLFW already provides the
        GLFW_CURSOR_DISABLED cursor mode that hides the cursor, transparently re-centers it and provides
        unconstrained cursor motion. See glfwSetInputMode for more information.

        If the cursor mode is GLFW_CURSOR_DISABLED then the cursor position is unconstrained and limited only by the
        minimum and maximum values of a double.

        Parameters
        ----------
        window: Window
            The desired window.
        xpos: float
            The desired x-coordinate, relative to the left edge of the client area.
        ypos: float
            The desired y-coordinate, relative to the top edge of the client area.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def create_cursor(self, image: Image, xhot: int, yhot: int) -> Cursor:
        """
        Creates a custom cursor.

        Creates a new custom cursor image that can be set for a window with glfwSetCursor.
        The cursor can be destroyed with glfwDestroyCursor. Any remaining cursors are destroyed by glfwTerminate.

        The pixels are 32-bit, little-endian, non-premultiplied RGBA, i.e. eight bits per channel.
        They are arranged canonically as packed sequential rows, starting from the top-left corner.

        The cursor hotspot is specified in pixels, relative to the upper-left corner of the cursor image.
        Like all other coordinate systems in GLFW, the X-axis points to the right and the Y-axis points down.

        Parameters
        ----------
        image: Image
            The desired cursor image.
        xhot: int
            The desired x-coordinate, in pixels, of the cursor hotspot.
        yhot: int
            The desired y-coordinate, in pixels, of the cursor hotspot.

        Returns
        -------
        cursor: Cursor
            The handle of the created cursor, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def create_standard_cursor(self, shape: int) -> Cursor:
        """
        Creates a cursor with a standard shape.

        Returns a cursor with a standard shape, that can be set for a window with glfwSetCursor.

        Parameters
        ----------
        shape: int
            One of the standard shapes.

        Returns
        -------
        A new cursor ready to use or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def destroy_cursor(self, cursor: Cursor):
        """
        Destroys a cursor.

        Parameters
        ----------
        cursor: Cursor
            The cursor object to destroy.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_cursor(self, window: Window, cursor: Cursor):
        """
        Sets the cursor for the window.

        This function sets the cursor image to be used when the cursor is over the client area of the specified window.
        The set cursor will only be visible when the cursor mode of the window is GLFW_CURSOR_NORMAL.

        On some platforms, the set cursor may not be visible unless the window also has input focus.

        Parameters
        ----------
        window: Window
            THe window to set the cursor for.
        cursor: Cursor
            The cursor to set, or NULL to switch back to the default arrow cursor.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_key_callback(self, window: Window, cbfun: KEY_CALLBACK) -> KEY_CALLBACK:
        """
        Sets the key callback.

        This function sets the key callback of the specified window, which is called when a key is pressed,
        repeated or released.

        The key functions deal with physical keys, with layout independent key tokens named after their values in the
        standard US keyboard layout. If you want to input text, use the character callback instead.

        When a window loses input focus, it will generate synthetic key release events for all pressed keys.
        You can tell these events from user-generated events by the fact that the synthetic ones are generated after
        the focus loss event has been processed, i.e. after the window focus callback has been called.

        The scancode of a key is specific to that platform or sometimes even to that machine. Scancodes are intended to
        allow users to bind keys that don't have a GLFW key token. Such keys have key set to GLFW_KEY_UNKNOWN, their
        state is not saved and so it cannot be queried with glfwGetKey.

        Sometimes GLFW needs to generate synthetic key events, in which case the scancode may be zero.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: KEY_CALLBACK
            The new key callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: KEY_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_char_callback(self, window: Window, cbfun: CHAR_CALLBACK) -> CHAR_CALLBACK:
        """
        Sets the Unicode character callback.

        This function sets the character callback of the specified window,
        which is called when a Unicode character is input.

        The character callback is intended for Unicode text input. As it deals with characters,
        it is keyboard layout dependent, whereas the key callback is not.
        Characters do not map 1:1 to physical keys, as a key may produce zero, one or more characters.
        If you want to know whether a specific physical key was pressed or released, see the key callback instead.

        The character callback behaves as system text input normally does and will not be called if modifier keys are
        held down that would prevent normal text input on that platform, for example a Super (Command) key on OS X or
        Alt key on Windows. There is a character with modifiers callback that receives these events.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: CHAR_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: CHAR_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_char_mods_callback(self, window: Window, cbfun: CHAR_MODS_CALLBACK) -> CHAR_MODS_CALLBACK:
        """
        Sets the Unicode character with modifiers callback.

        This function sets the character with modifiers callback of the specified window,
        which is called when a Unicode character is input regardless of what modifier keys are used.

        The character with modifiers callback is intended for implementing custom Unicode character input.
        For regular Unicode text input, see the character callback. Like the character callback,
        the character with modifiers callback deals with characters and is keyboard layout dependent.
        Characters do not map 1:1 to physical keys, as a key may produce zero, one or more characters.
        If you want to know whether a specific physical key was pressed or released, see the key callback instead.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: CHAR_MODS_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: CHAR_MODS_CALLBACK
            The previously set callback, or NULL if no callback was set or an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_mouse_button_callback(self, window: Window, cbfun: MOUSE_BUTTON_CALLBACK) -> MOUSE_BUTTON_CALLBACK:
        """
        Sets the mouse button callback.

        This function sets the mouse button callback of the specified window,
        which is called when a mouse button ispressed or released.

        When a window loses input focus, it will generate synthetic mouse button release events for all pressed
        mouse buttons. You can tell these events from user-generated events by the fact that the synthetic ones are
        generated after the focus loss event has been processed, i.e. after the window focus callback has been called.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: MOUSE_BUTTON_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: MOUSE_BUTTON_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_cursor_pos_callback(self, window: Window, cbfun: CURSOR_POSITION_CALLBACK) -> CURSOR_POSITION_CALLBACK:
        """
        Sets the cursor position callback.

        This function sets the cursor position callback of the specified window, which is called when the cursor is
        moved. The callback is provided with the position, in screen coordinates, relative to the upper-left corner
        of the client area of the window.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: CURSOR_POSITION_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: CURSOR_POSITION_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_cursor_enter_callback(self, window: Window, cbfun: CURSOR_ENTER_CALLBACK) -> CURSOR_ENTER_CALLBACK:
        """
        Sets the cursor enter/exit callback.

        This function sets the cursor boundary crossing callback of the specified window,
        which is called when the cursor enters or leaves the client area of the window.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: CURSOR_ENTER_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_scroll_callback(self, window: Window, cbfun: SCROLL_CALLBACK) -> SCROLL_CALLBACK:
        """
        Sets the scroll callback.

        This function sets the scroll callback of the specified window, which is called when a scrolling device is used,
        such as a mouse wheel or scrolling area of a touchpad.

        The scroll callback receives all scrolling input, like that from a mouse wheel or a touchpad scrolling area.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: SCROLL_CALLBACK
            The new scroll callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: SCROLL_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_drop_callback(self, window: Window, cbfun: DROP_CALLBACK) -> DROP_CALLBACK:
        """
        Sets the file drop callback.

        This function sets the file drop callback of the specified window, which is called when one or more dragged
        files are dropped on the window.

        Because the path array and its strings may have been generated specifically for that event,
        they are not guaranteed to be valid after the callback has returned.
        If you wish to use them after the callback returns, you need to make a deep copy.

        Parameters
        ----------
        window: Window
            The window whose callback to set.
        cbfun: DROP_CALLBACK
            The new file drop callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: DROP_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def joystick_present(self, joy: int) -> int:
        """
        Returns whether the specified joystick is present.

        This function returns whether the specified joystick is present.

        Parameters
        ----------
        joy: int
            The joystick to query.

        Returns
        -------
        present: int
            GLFW_TRUE if the joystick is present, or GLFW_FALSE otherwise.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_joystick_axes(self, joy: int, count: POINTER(c_int)) -> POINTER(c_float):
        """
        Returns the values of all axes of the specified joystick.

        This function returns the values of all axes of the specified joystick.
        Each element in the array is a value between -1.0 and 1.0.

        Querying a joystick slot with no device present is not an error, but will cause this function to return NULL.
        Call glfwJoystickPresent to check device presence.

        Parameters
        ----------
        joy: int
            The joystick to query.
        count: POINTER(c_int)
            Where to store the number of axis values in the returned array.
            This is set to zero if the joystick is not present or an error occurred.

        Returns
        -------
        axes: POINTER(c_float)
            An array of axis values, or NULL if the joystick is not present or an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_joystick_buttons(self, joy: int, count: POINTER(c_int)) -> POINTER(c_ubyte):
        """
        Returns the state of all buttons of the specified joystick.

        This function returns the state of all buttons of the specified joystick.
        Each element in the array is either GLFW_PRESS or GLFW_RELEASE.

        Querying a joystick slot with no device present is not an error,but will cause this function to return NULL.
        Call glfwJoystickPresent to check device presence.

        Parameters
        ----------
        joy: int
            The joystick to query
        count: POINTER(c_int)
            Where to store the number of button states in the returned array.
            This is set to zero if the joystick is not present or an error occurred.

        Returns
        -------
        buttons: POINTER(c_ubyte)
            An array of button states, or NULL if the joystick is not present or an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_joystick_name(self, joy: int) -> bytes:
        """
        Returns the name of the specified joystick.

        This function returns the name, encoded as UTF-8, of the specified joystick.
        The returned string is allocated and freed by GLFW. You should not free it yourself.

        Querying a joystick slot with no device present is not an error, but will cause this function to return NULL.
        Call glfwJoystickPresent to check device presence.

        Parameters
        ----------
        joy: int
            The joystick to query

        Returns
        -------
        name: bytes
            The UTF-8 encoded name of the joystick, or NULL if the joystick is not present or an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_ENUM and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_joystick_callback(self, cbfun: JOYSTICK_CALLBACK) -> JOYSTICK_CALLBACK:
        """
        Sets the joystick configuration callback.

        This function sets the joystick configuration callback, or removes the currently set callback.
        This is called when a joystick is connected to or disconnected from the system.

        Parameters
        ----------
        cbfun: JOYSTICK_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: JOYSTICK_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_clipboard_string(self, window: Window, string: bytes):
        """
        Sets the clipboard to the specified string.

        This function sets the system clipboard to the specified, UTF-8 encoded string.

        Parameters
        ----------
        window: Window
            The window that will own the clipboard contents.
        string: bytes
            A UTF-8 encoded string.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_clipboard_string(self, window: Window) -> bytes:
        """
        Returns the contents of the clipboard as a string.

        This function returns the contents of the system clipboard, if it contains or is convertible to a UTF-8 encoded
        string. If the clipboard is empty or if its contents cannot be converted,
        NULL is returned and a GLFW_FORMAT_UNAVAILABLE error is generated.

        Parameters
        ----------
        window: Window
            The window that will request the clipboard contents.

        Returns
        -------
        clipboard_string: bytes
            The contents of the clipboard as a UTF-8 encoded string, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_time(self) -> float:
        """
        Returns the value of the GLFW timer.

        This function returns the value of the GLFW timer. Unless the timer has been set using glfwSetTime,
        the timer measures time elapsed since GLFW was initialized

        The resolution of the timer is system dependent, but is usually on the order of a few micro- or nanoseconds.
        It uses the highest-resolution monotonic time source on each supported platform.

        Returns
        -------
        time: float
            The current value, in seconds, or zero if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_time(self, time: float):
        """
        Sets the GLFW timer.

        This function sets the value of the GLFW timer. It then continues to count up from that value.
        The value must be a positive finite number less than or equal to 18446744073.0,
        which is approximately 584.5 years.

        Parameters
        ----------
        time: float
            The new value, in seconds.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_INVALID_VALUE.

        Notes
        -----
        The upper limit of the timer is calculated as floor((2^64 - 1) / 10^9) and is due to
        implementations storing nanoseconds in 64 bits. The limit may be increased in the future.
        """
        pass

    def get_timer_value(self) -> c_uint64:
        """
        Returns the current value of the raw timer.

        This function returns the current value of the raw timer, measured in 1 / frequency seconds.
        To get the frequency, call glfwGetTimerFrequency.

        Returns
        -------
        value: c_uint64
            The value of the timer, or zero if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def get_timer_frequency(self) -> c_uint64:
        """
        Returns the frequency, in Hz, of the raw timer.

        This function returns the frequency, in Hz, of the raw timer.

        Returns
        -------
        frequency: c_uint64
            The frequency of the timer, in Hz, or zero if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def get_monitors(self, count: POINTER(c_int)) -> POINTER(Monitor):
        """
        Returns the currently connected monitors.

        This function returns an array of handles for all currently connected monitors.
        The primary monitor is always first in the returned array.
        If no monitors were found, this function returns NULL.

        Parameters
        ----------
        count: POINTER(c_int)
            Where to store the number of monitors in the returned array. This is set to zero if an error occurred.

        Returns
        -------
        monitors: POINTER(Monitor)
            An array of monitor handles, or NULL if no monitors were found or if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def get_primary_monitor(self) -> Monitor:
        """
        Returns the primary monitor.

        This function returns the primary monitor.
        This is usually the monitor where elements like the task bar or global menu bar are located.

        Returns
        -------
        monitor: Monitor
            The primary monitor, or NULL if no monitors were found or if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.

        Notes
        -----
        The primary monitor is always first in the array returned by glfwGetMonitors.
        """

    def get_monitor_pos(self, monitor: Monitor, xpos: POINTER(c_int), ypos: POINTER(c_int)):
        """
        Returns the position of the monitor's viewport on the virtual screen.

        This function returns the position, in screen coordinates, of the upper-left corner of the specified monitor.

        Any or all of the position arguments may be NULL.
        If an error occurs, all non-NULL position arguments will be set to zero.

        Parameters
        ----------
        monitor: Monitor
            The monitor to query.
        xpos: POINTER(c_int)
            Where to store the monitor x-coordinate, or NULL.
        ypos: POINTER(c_int)
            Where to store the monitor y-coordinate, or NULL.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_monitor_physical_size(self, monitor: Monitor, width: POINTER(c_int), height: POINTER(c_int)):
        """
        Returns the physical size of the monitor.

        This function returns the size, in millimetres, of the display area of the specified monitor.

        Some systems do not provide accurate monitor size information, either because the monitor EDID data is
        incorrect or because the driver does not report it accurately.

        Any or all of the size arguments may be NULL.
        If an error occurs,all non-NULL size arguments will be set to zero.

        Parameters
        ----------
        monitor: Monitor
        width: int
        height: int

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.

        Notes
        -----
        Windows: calculates the returned physical size from the current resolution and system DPI
                 instead of querying the monitor EDID data.

        """
        pass

    def get_monitor_name(self, monitor: Monitor) -> bytes:
        """
        Returns the name of the specified monitor.

        This function returns a human-readable name, encoded as UTF-8, of the specified monitor.
        The name typically reflects the make and model of the monitor and
        is not guaranteed to be unique among the connected monitors.

        Parameters
        ----------
        monitor: Monitor
            The monitor to query.

        Returns
        -------
        name: bytes
            The UTF-8 encoded name of the monitor, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def set_monitor_callback(self, cbfun: MONITOR_CALLBACK) -> MONITOR_CALLBACK:
        """
        Sets the monitor configuration callback.

        This function sets the monitor configuration callback, or removes the currently set callback.
        This is called when a monitor is connected to or disconnected from the system.

        Parameters
        ----------
        cbfun: MONITOR_CALLBACK
            The new callback, or NULL to remove the currently set callback.

        Returns
        -------
        cbfun: MONITOR_CALLBACK
            The previously set callback, or NULL if no callback was set or the library had not been initialized.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED.
        """
        pass

    def get_video_modes(self, monitor: Monitor, count: POINTER(c_int)) -> POINTER(VideoMode):
        """
        Returns the available video modes for the specified monitor.

        This function returns an array of all video modes supported by the specified monitor.
        The returned array is sorted in ascending order, first by color bit depth (the sum of all channel depths)
        and then by resolution area (the product of width and height).

        Parameters
        ----------
        monitor: Monitor
            The monitor to query.
        count: POINTER(c_int)
            Where to store the number of video modes in the returned array. This is set to zero if an error occurred.

        Returns
        -------
        video_modes: POINTER(VideoMode)
            An array of video modes, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_video_mode(self, monitor: Monitor) -> VideoMode:
        """
        Returns the current mode of the specified monitor.

        This function returns the current video mode of the specified monitor.
        If you have created a full screen window for that monitor,
        the return value will depend on whether that window is iconified.

        Parameters
        ----------
        monitor: Monitor
            The monitor to query.

        Returns
        -------
        video_mode: VideoMode
            The current mode of the monitor, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_gamma(self, monitor: Monitor, gamma: float):
        """
        Generates a gamma ramp and sets it for the specified monitor.

        This function generates a 256-element gamma ramp from the specified exponent
        and then calls glfwSetGammaRamp with it.
        The value must be a finite number greater than zero.

        Parameters
        ----------
        monitor: Monitor
            The monitor whose gamma ramp to set.
        gamma: float
            The desired exponent.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED, GLFW_INVALID_VALUE and GLFW_PLATFORM_ERROR.
        """
        pass

    def get_gamma_ramp(self, monitor: Monitor) -> GammaRamp:
        """
        Returns the current gamma ramp for the specified monitor.

        This function returns the current gamma ramp of the specified monitor.

        Parameters
        ----------
        monitor: Monitor
            The monitor to query.

        Returns
        -------
        ramp: GammaRamp
            The current gamma ramp, or NULL if an error occurred.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.
        """
        pass

    def set_gamma_ramp(self, monitor: Monitor, ramp: GammaRamp):
        """
        Sets the current gamma ramp for the specified monitor.

        This function sets the current gamma ramp for the specified monitor.
        The original gamma ramp for that monitor is saved by GLFW the first time this function is called
        and is restored by glfwTerminate.

        Parameters
        ----------
        monitor: Monitor
            The monitor whose gamma ramp to set.
        ramp: GammaRamp
            The gamma ramp to use.

        Raises
        ------
        Possible errors include GLFW_NOT_INITIALIZED and GLFW_PLATFORM_ERROR.

        Notes
        -----
        Gamma ramp sizes other than 256 are not supported by all platforms or graphics hardware.
        Windows: The gamma ramp size must be 256.
        """
        pass

    def _wrap(self, target: Callable, function_name: str, return_type=None, *argument_types):
        """
        Wrap glfw function

        This function wraps a glfw function using the following steps:
            1. Get glfw function pointer from glfw dll
            2. Specify return & argument types using ctypes
            3. Override Python function with wrapped glfw function

        This has the following benefits:
            1. Functions can be specified in an user/IDE friendly fashion, including Python-Numpy documentation.
            2. Function calls are directly pointed to the ctypes function, which saves a function call each call.

        Parameters
        ----------
        target: Callable
            Python function handle
        function_name: str
            Name of glfw function in glfw library: e.g. 'glfwFooBar'
        return_type: ctypes type
            Return type as ctypes type or None for void
        argument_types: ctypes types
            Argument types as ctypes types
        """
        func = self._dll.__getattr__(function_name)
        func.restype, func.argtypes = return_type, argument_types
        self.__setattr__(target.__name__, func)

    def _wrap_all(self):
        """Wraps all supported glfw functions"""

        self._wrap(self.extension_supported, 'glfwExtensionSupported',
                   c_int, c_char_p)
        self._wrap(self.get_current_context, 'glfwGetCurrentContext',
                   POINTER(Window))
        self._wrap(self.get_proc_address, 'glfwGetProcAddress',
                   c_void_p, c_char_p)
        self._wrap(self.make_context_current, 'glfwMakeContextCurrent',
                   None, POINTER(Window))
        self._wrap(self.swap_interval, 'glfwSwapInterval',
                   None, c_void_p)

        self._wrap(self.init, 'glfwInit',
                   c_int)
        self._wrap(self.terminate, 'glfwTerminate')
        self._wrap(self.get_version, 'glfwGetVersion',
                   None, POINTER(c_int), POINTER(c_int), POINTER(c_int))
        self._wrap(self.get_version_string, 'glfwGetVersionString',
                   c_char_p)
        self._wrap(self.set_error_callback, 'glfwSetErrorCallback',
                   self.ERROR_CALLBACK, self.ERROR_CALLBACK)

        self._wrap(self.default_window_hints, 'glfwDefaultWindowHints')
        self._wrap(self.window_hint, 'glfwWindowHint',
                   None, c_int, c_int)
        self._wrap(self.create_window, 'glfwCreateWindow',
                   POINTER(Window), c_int, c_int, c_char_p, POINTER(Monitor), POINTER(Window))
        self._wrap(self.destroy_window, 'glfwDestroyWindow',
                   None, POINTER(Window))
        self._wrap(self.window_should_close, 'glfwWindowShouldClose',
                   c_int, POINTER(Window))
        self._wrap(self.set_window_should_close, 'glfwSetWindowShouldClose',
                   None, POINTER(Window))
        self._wrap(self.set_window_title, 'glfwSetWindowTitle',
                   None, POINTER(Window), c_char_p)
        self._wrap(self.set_window_icon, 'glfwSetWindowIcon',
                   None, POINTER(Window), c_int, POINTER(Image))
        self._wrap(self.get_window_pos, 'glfwGetWindowPos',
                   None, POINTER(Window), POINTER(c_int), POINTER(c_int))
        self._wrap(self.set_window_pos, 'glfwSetWindowPos',
                   None, POINTER(Window), c_int, c_int)
        self._wrap(self.set_window_size_limits, 'glfwSetWindowSizeLimits',
                   None, POINTER(Window), c_int, c_int, c_int, c_int)
        self._wrap(self.set_window_aspect_ratio, 'glfwSetWindowAspectRatio',
                   None, POINTER(Window), c_int, c_int)
        self._wrap(self.set_window_size, 'glfwSetWindowSize',
                   None, POINTER(Window), c_int, c_int)
        self._wrap(self.get_framebuffer_size, 'glfwGetFramebufferSize',
                   None, POINTER(Window), POINTER(c_int), POINTER(c_int))
        self._wrap(self.get_window_frame_size, 'glfwGetWindowFrameSize',
                   None, POINTER(Window), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
        self._wrap(self.iconify_window, 'glfwIconifyWindow',
                   None, POINTER(Window))
        self._wrap(self.restore_window, 'glfwRestoreWindow',
                   None, POINTER(Window))
        self._wrap(self.maximize_window, 'glfwMaximizeWindow',
                   None, POINTER(Window))
        self._wrap(self.show_window, 'glfwShowWindow',
                   None, POINTER(Window))
        self._wrap(self.hide_window, 'glfwHideWindow',
                   None, POINTER(Window))
        self._wrap(self.focus_window, 'glfwFocusWindow',
                   None, POINTER(Window))
        self._wrap(self.get_window_monitor, 'glfwGetWindowMonitor',
                   POINTER(Monitor), POINTER(Window))
        self._wrap(self.set_window_monitor, 'glfwSetWindowMonitor',
                   POINTER(Window), POINTER(Monitor), c_int, c_int, c_int, c_int, c_int)
        self._wrap(self.get_window_attribute, 'glfwGetWindowAttrib',
                   c_int, POINTER(Window), c_int)
        self._wrap(self.set_window_user_pointer, 'glfwSetWindowUserPointer',
                   None, POINTER(Window), c_void_p)
        self._wrap(self.get_window_user_pointer, 'glfwGetWindowUserPointer',
                   c_void_p, POINTER(Window))
        self._wrap(self.set_window_pos_callback, 'glfwSetWindowPosCallback',
                   self.WINDOW_POSITION_CALLBACK, POINTER(Window), self.WINDOW_POSITION_CALLBACK, )
        self._wrap(self.set_window_size_callback, 'glfwSetWindowSizeCallback',
                   self.WINDOW_SIZE_CALLBACK, POINTER(Window), self.WINDOW_SIZE_CALLBACK)
        self._wrap(self.set_window_close_callback, 'glfwSetWindowCloseCallback',
                   self.WINDOW_CLOSE_CALLBACK, POINTER(Window), self.WINDOW_CLOSE_CALLBACK)
        self._wrap(self.set_window_refresh_callback, 'glfwSetWindowRefreshCallback',
                   self.WINDOW_REFRESH_CALLBACK, POINTER(Window), self.WINDOW_REFRESH_CALLBACK)
        self._wrap(self.set_window_focus_callback, 'glfwSetWindowFocusCallback',
                   self.WINDOW_FOCUS_CALLBACK, POINTER(Window), self.WINDOW_FOCUS_CALLBACK)
        self._wrap(self.set_window_iconify_callback, 'glfwSetWindowIconifyCallback',
                   self.WINDOW_ICONIFY_CALLBACK, POINTER(Window), self.WINDOW_ICONIFY_CALLBACK)
        self._wrap(self.set_framebuffer_size_callback, 'glfwSetFramebufferSizeCallback',
                   self.FRAMEBUFFER_SIZE_CALLBACK, POINTER(Window), self.FRAMEBUFFER_SIZE_CALLBACK)
        self._wrap(self.poll_events, 'glfwPollEvents')
        self._wrap(self.wait_events, 'glfwWaitEvents')
        self._wrap(self.wait_events_timeout, 'glfwWaitEventsTimeout',
                   None, c_double)
        self._wrap(self.post_empty_event, 'glfwPostEmptyEvent')
        self._wrap(self.swap_buffers, 'glfwSwapBuffers',
                   None, POINTER(Window))

        self._wrap(self.get_input_mode, 'glfwGetInputMode',
                   c_int, POINTER(Window), c_int)
        self._wrap(self.set_input_mode, 'glfwSetInputMode',
                   None, POINTER(Window), c_int, c_int)
        self._wrap(self.get_key_name, 'glfwGetKeyName',
                   c_char_p, c_int, c_int)
        self._wrap(self.get_key, 'glfwGetKey',
                   c_int, POINTER(Window), c_int)
        self._wrap(self.get_mouse_button, 'glfwGetMouseButton',
                   c_int, POINTER(Window), c_int)
        self._wrap(self.get_cursor_pos, 'glfwGetCursorPos',
                   None, POINTER(Window), POINTER(c_double), POINTER(c_double))
        self._wrap(self.set_cursor_pos, 'glfwSetCursorPos',
                   None, POINTER(Window), c_double, c_double)
        self._wrap(self.create_cursor, 'glfwCreateCursor',
                   POINTER(Cursor), POINTER(Image), c_int, c_int)
        self._wrap(self.create_standard_cursor, 'glfwCreateStandardCursor',
                   POINTER(Cursor), c_int)
        self._wrap(self.destroy_cursor, 'glfwDestroyCursor',
                   None, POINTER(Cursor))
        self._wrap(self.set_cursor, 'glfwSetCursor',
                   None, POINTER(Window), POINTER(Cursor))
        self._wrap(self.set_key_callback, 'glfwSetKeyCallback',
                   self.KEY_CALLBACK, POINTER(Window), self.KEY_CALLBACK)
        self._wrap(self.set_char_callback, 'glfwSetCharCallback',
                   self.CHAR_CALLBACK, POINTER(Window), self.CHAR_CALLBACK)
        self._wrap(self.set_char_mods_callback, 'glfwSetCharModsCallback',
                   self.CHAR_MODS_CALLBACK, POINTER(Window), self.CHAR_MODS_CALLBACK)
        self._wrap(self.set_mouse_button_callback, 'glfwSetMouseButtonCallback',
                   self.MOUSE_BUTTON_CALLBACK, POINTER(Window), self.MOUSE_BUTTON_CALLBACK)
        self._wrap(self.set_cursor_pos_callback, 'glfwSetCursorPosCallback',
                   self.CURSOR_POSITION_CALLBACK, POINTER(Window), self.CURSOR_POSITION_CALLBACK)
        self._wrap(self.set_cursor_enter_callback, 'glfwSetCursorEnterCallback',
                   self.CURSOR_ENTER_CALLBACK, POINTER(Window), self.CURSOR_ENTER_CALLBACK)
        self._wrap(self.set_scroll_callback, 'glfwSetScrollCallback',
                   self.SCROLL_CALLBACK, POINTER(Window), self.SCROLL_CALLBACK)
        self._wrap(self.set_drop_callback, 'glfwSetDropCallback',
                   self.DROP_CALLBACK, POINTER(Window), self.DROP_CALLBACK)
        self._wrap(self.joystick_present, 'glfwJoystickPresent',
                   c_int, c_int)
        self._wrap(self.get_joystick_axes, 'glfwGetJoystickAxes',
                   POINTER(c_float), c_int, POINTER(c_int))
        self._wrap(self.get_joystick_buttons, 'glfwGetJoystickButtons',
                   POINTER(c_ubyte), c_int, POINTER(c_int))
        self._wrap(self.get_joystick_name, 'glfwGetJoystickName',
                   c_char_p, c_int)
        self._wrap(self.set_joystick_callback, 'glfwSetJoystickCallback',
                   self.JOYSTICK_CALLBACK, self.JOYSTICK_CALLBACK)
        self._wrap(self.set_clipboard_string, 'glfwSetClipboardString',
                   None, POINTER(Window), c_char_p)
        self._wrap(self.get_clipboard_string, 'glfwGetClipboardString',
                   c_char_p, POINTER(Window))
        self._wrap(self.get_time, 'glfwGetTime',
                   c_double)
        self._wrap(self.set_time, 'glfwSetTime',
                   None, c_double)
        self._wrap(self.get_timer_value, 'glfwGetTimerValue',
                   c_uint64)
        self._wrap(self.get_timer_frequency, 'glfwGetTimerFrequency',
                   c_uint64)

        self._wrap(self.get_monitors, 'glfwGetMonitors',
                   POINTER(POINTER(Monitor)), POINTER(c_int))
        self._wrap(self.get_primary_monitor, 'glfwGetPrimaryMonitor',
                   POINTER(Monitor))
        self._wrap(self.get_monitor_pos, 'glfwGetMonitorPos',
                   None, POINTER(Monitor), POINTER(c_int), POINTER(c_int))
        self._wrap(self.get_monitor_physical_size, 'glfwGetMonitorPhysicalSize',
                   None, POINTER(Monitor), POINTER(c_int), POINTER(c_int))
        self._wrap(self.get_monitor_name, 'glfwGetMonitorName',
                   c_char_p, POINTER(Monitor))
        self._wrap(self.set_monitor_callback, 'glfwSetMonitorCallback',
                   self.MONITOR_CALLBACK, self.MONITOR_CALLBACK)
        self._wrap(self.get_video_modes, 'glfwGetVideoModes',
                   POINTER(VideoMode), POINTER(Monitor), POINTER(c_int))
        self._wrap(self.get_video_mode, 'glfwGetVideoMode',
                   POINTER(VideoMode), POINTER(Monitor))
        self._wrap(self.set_gamma, 'glfwSetGamma',
                   None, POINTER(Monitor), c_float)
        self._wrap(self.get_gamma_ramp, 'glfwGetGammaRamp',
                   POINTER(GammaRamp), POINTER(Monitor))
        self._wrap(self.set_gamma_ramp, 'glfwSetGammaRamp',
                   None, POINTER(Monitor), POINTER(GammaRamp))

    def _error_callback(self, code: int, description: bytes):
        """
        Error callback function

        Call appropriate GLFW Exception when one should occur

        Parameters
        ----------
        code: int
            An error code.
        description: bytes
            A UTF-8 encoded string describing the error.
        """
        raise self._ERROR[code](description.decode())

    def __enter__(self):
        """
        Initialize GLFW library on with-statement.

        Returns
        -------
        glfw: GLFW
            The initialized GLFW library
        """
        self.init()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Terminate GLFW library on with-statement exit."""
        self.terminate()

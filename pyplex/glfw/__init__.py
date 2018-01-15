import ctypes
import os


# ..:: GLFW Library Paths ::.. #
PATH_GLFW_WIN = os.path.join(os.path.dirname(__file__), 'bin', 'glfw3_x64.dll')

# ..:: GLFW Library Loading ::.. #
_glfw = ctypes.CDLL(PATH_GLFW_WIN)

# ..:: Error Handling ::.. #
# TODO: Test if this works!
class GLFWError(Exception): pass

def _glfw_error_handler(code: int, description: str):
    raise GLFWError("[{}] {}".format(code, description))

_glfw_error_function = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
_glfw.glfwSetErrorCallback.restype = _glfw_error_function
_glfw.glfwSetErrorCallback.argtypes = [_glfw_error_function]
_glfw.glfwSetErrorCallback(_glfw_error_function(_glfw_error_handler))


from .contants import *
from .functions import *

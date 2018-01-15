from pyplex import Canvas, Button, Key, Action, Modifier
import numpy as np


class VerboseCanvas(Canvas):
    def __init__(self):
        """Verbose Canvas Events Example"""
        super().__init__(wait_for_events=True)

    def on_draw(self):
        print("on_draw")

    def on_update(self, dt: float):
        print("on_update", dt)

    def on_mouse_move(self, position: np.ndarray):
        print("on_mouse_move", position)

    def on_mouse_button(self, button: Button, action: Action, modifier: Modifier):
        print("on_mouse_button", button, action, modifier)

    def on_scroll(self, offset: np.ndarray):
        print("on_scroll", offset)

    def on_key(self, key: Key, action: Action, modifier: Modifier):
        print("on_key", key, action, modifier)

    def on_char(self, char: str):
        print("on_char", char)

    def on_window_move(self, position: np.ndarray):
        print("on_window_move", position)

    def on_resize(self, size: np.ndarray):
        print("on_resize", size)

    def on_framebuffer_resize(self, size: np.ndarray):
        print("on_framebuffer_resize", size)

    def on_refresh(self):
        print("on_refresh")

    def on_focus(self, value: bool):
        print("on_focus", value)

    def on_iconify(self, value: bool):
        print("on_iconify", value)

    def on_close(self):
        print("on_close")


if __name__ == "__main__":
    with VerboseCanvas() as canvas:
        canvas.run()

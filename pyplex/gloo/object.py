from pyplex import gl


class Object:
    @property
    def ctx(self) -> gl.Context:
        raise NotImplementedError()

    @property
    def ptr(self) -> gl.Object:
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def __del__(self):
        self.delete()


class ContextObject(Object):
    def bind(self):
        raise NotImplementedError()

    def unbind(self):
        raise NotImplementedError()

    def __enter__(self):
        self.bind()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unbind()
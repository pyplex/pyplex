from pyplex.glow import UniformBuffer


class UniformObject:
    @property
    def type(self) -> str:
        return self.__class__.__name__

    @property
    def buffer(self) -> UniformBuffer:
        raise NotImplementedError()
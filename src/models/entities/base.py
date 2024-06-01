class Base:
    def __repr__(self) -> str:
        cls = self.__class__
        attributes = self.__dict__
        attributes_str = ", ".join(f"{key}={value!r}" for key, value in attributes.items())
        return f"{cls.__name__}({attributes_str})"
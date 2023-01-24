from typing import TypeVar, Callable, Generic, Iterable

ValueType = TypeVar("ValueType")
FunctionReturnType = TypeVar("FunctionReturnType")


class Pipe(Generic[ValueType]):
    def __init__(self, initial_value: ValueType) -> None:
        self._value: ValueType = initial_value
        self.p = self.pipe

    def pipe(self, function: Callable[[ValueType], FunctionReturnType]):
        result: FunctionReturnType = function(self._value)
        return Pipe(result)

    def check(self, function: Callable[[ValueType], FunctionReturnType]):
        function(self._value)
        return Pipe(self._value)

    def unpack(self):
        return self._value


P = Pipe

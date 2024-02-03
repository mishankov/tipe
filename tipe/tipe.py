from typing import TypeVar, Callable, Generic

ValueType = TypeVar("ValueType")
FunctionReturnType = TypeVar("FunctionReturnType")


class Pipe(Generic[ValueType]):
    def __init__(self, initial_value: ValueType) -> None:
        self._value: ValueType = initial_value
        self.p = self.pipe
        self.c = self.check
        self.u = self.unwrap

    def pipe(
        self,
        function: Callable[[ValueType], FunctionReturnType],
        *additional_params: list,
    ):
        result = function(self._value, *additional_params)

        return Pipe(result)

    def check(
        self,
        function: Callable[[ValueType], FunctionReturnType],
        *additional_params: list,
    ):
        function(self._value, *additional_params)
        return Pipe(self._value)

    def unwrap(self):
        return self._value

    def __repr__(self) -> str:
        return f"Pipe({self._value})"


P = Pipe

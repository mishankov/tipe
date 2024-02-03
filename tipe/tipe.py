from typing import TypeVar, Callable, Generic

ValueType = TypeVar("ValueType")
FunctionReturnType = TypeVar("FunctionReturnType")


class Pipe(Generic[ValueType]):
    def __init__(self, initial_value: ValueType) -> None:
        """
        Initializes the object with the initial value and sets up aliases for pipe, check, and unwrap functions.
        
        :param initial_value: The initial value to be assigned to the object.
        :type initial_value: ValueType
        :return: None
        """
        self._value: ValueType = initial_value
        self.p = self.pipe
        self.c = self.check
        self.u = self.unwrap

    def pipe(
        self,
        function: Callable[[ValueType], FunctionReturnType],
        *additional_params: list,
    ):
        """
        Applies a function to the value of the Pipe object and returns a new Pipe object.

        Args:
            function (Callable[[ValueType], FunctionReturnType]): The function to apply to the value.
            *additional_params (list): Additional parameters to pass to the function.

        Returns:
            Pipe: A new Pipe object with the result of applying the function to the value.
        """
        result = function(self._value, *additional_params)

        return Pipe(result)

    def check(
        self,
        function: Callable[[ValueType], FunctionReturnType],
        *additional_params: list,
    ):
        """
        Apply the given function to the current value and return the result as a new Pipe.
        
        Args:
            function: The function to apply to the current value.
            *additional_params: Additional parameters to pass to the function.
        
        Returns:
            Pipe: A new Pipe containing the result of applying the function to the current value.
        """
        function(self._value, *additional_params)
        return Pipe(self._value)

    def unwrap(self):
        """
        Return the value of the wrapped object.
        """
        return self._value

    def __repr__(self) -> str:
        """
        Return a string representation of the Pipe object.
        """
        return f"Pipe({self._value})"


P = Pipe

import reflex as rx
from typing import Optional

class State(rx.State):
    """The app state for the calculator."""
    display: str = "0"
    first_number: Optional[float] = None
    operation: Optional[str] = None
    new_number: bool = False

    def append_digit(self, digit: str):
        """Append a digit to the display."""
        if self.new_number or self.display == "0":
            self.display = digit
            self.new_number = False
        else:
            self.display += digit

    def set_operation(self, op: str):
        """Set the operation to perform."""
        self.first_number = float(self.display)
        self.operation = op
        self.new_number = True

    def clear(self):
        """Clear the calculator state."""
        self.display = "0"
        self.first_number = None
        self.operation = None
        self.new_number = False

    def calculate(self):
        """Perform the calculation."""
        if self.operation and self.first_number is not None:
            second_number = float(self.display)
            if self.operation == "+":
                result = self.first_number + second_number
            elif self.operation == "-":
                result = self.first_number - second_number
            elif self.operation == "*":
                result = self.first_number * second_number
            elif self.operation == "/":
                result = self.first_number / second_number if second_number != 0 else "Error"
            
            self.display = str(result).rstrip('0').rstrip('.') if isinstance(result, float) else str(result)
            self.first_number = None
            self.operation = None
            self.new_number = True

from .models import CalculationType

class CalculationError(Exception):
    pass

def compute_result(a: float, b: float, calc_type: CalculationType) -> float:
    if calc_type == CalculationType.ADD:
        return a + b
    if calc_type == CalculationType.SUB:
        return a - b
    if calc_type == CalculationType.MULTIPLY:
        return a * b
    if calc_type == CalculationType.DIVIDE:
        if b == 0:
            raise CalculationError("Division by zero")
        return a / b
    raise CalculationError(f"Unknown calculation type: {calc_type}")

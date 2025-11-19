import pytest
from app.factory import compute_result, CalculationError
from app.schemas import CalculationCreate, CalculationRead
from app.models import CalculationType

def test_add():
    assert compute_result(2, 3, CalculationType.ADD) == 5

def test_sub():
    assert compute_result(5, 3, CalculationType.SUB) == 2

def test_multiply():
    assert compute_result(2, 3, CalculationType.MULTIPLY) == 6

def test_divide():
    assert compute_result(6, 3, CalculationType.DIVIDE) == 2

def test_divide_by_zero_raises():
    with pytest.raises(CalculationError):
        compute_result(1, 0, CalculationType.DIVIDE)

def test_schema_validation_success():
    data = {"a": 2.0, "b": 3.0, "type": "Add"}
    c = CalculationCreate(**data)
    assert c.a == 2.0
    assert c.type == CalculationType.ADD

def test_schema_divide_by_zero_validator():
    with pytest.raises(ValueError):
        CalculationCreate(a=1.0, b=0.0, type="Divide")

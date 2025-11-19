# app/schemas.py
from pydantic import BaseModel, root_validator
from typing import Optional
from .models import CalculationType

class CalculationCreate(BaseModel):
    a: float
    b: float
    type: CalculationType

    # run this validator before Pydantic converts/validates fields (pre=True)
    @root_validator(pre=True)
    def check_divide_by_zero(cls, values):
        """
        This validator runs before parsing, so `type` might be a string like "Divide".
        We check both string names and enum values for division-by-zero.
        """
        t = values.get("type")
        b = values.get("b")

        # Normalize type value so we can compare robustly
        if isinstance(t, CalculationType):
            t_name = t.name  # e.g. 'DIVIDE'
        elif isinstance(t, str):
            t_name = t.strip().upper()
        else:
            t_name = None

        if t_name == "DIVIDE" and b == 0:
            raise ValueError("Division by zero is not allowed.")
        return values

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: CalculationType
    result: Optional[float] = None

    class Config:
        orm_mode = True

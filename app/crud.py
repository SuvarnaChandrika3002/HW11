from sqlalchemy.orm import Session
from .models import Calculation, CalculationType
from .schemas import CalculationCreate
from .factory import compute_result

def create_calculation(db: Session, calc_in: CalculationCreate) -> Calculation:
    result = compute_result(calc_in.a, calc_in.b, calc_in.type)
    calc = Calculation(a=calc_in.a, b=calc_in.b, type=calc_in.type, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

def get_calculation(db: Session, calc_id: int):
    return db.query(Calculation).filter(Calculation.id == calc_id).first()

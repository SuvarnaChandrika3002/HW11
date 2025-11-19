from sqlalchemy import Column, Integer, Float, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import enum

class CalculationType(str, enum.Enum):
    ADD = "Add"
    SUB = "Sub"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(Enum(CalculationType), nullable=False)
    result = Column(Float, nullable=True)

   

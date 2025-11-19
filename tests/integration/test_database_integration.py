import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Calculation
from app.schemas import CalculationCreate
from app.crud import create_calculation, get_calculation
from app.models import CalculationType

@pytest.fixture(scope="module")
def db_engine():
    database_url = os.getenv("DATABASE_URL", "sqlite+pysqlite:///./test.db")
    engine = create_engine(database_url, future=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture()
def db_session(db_engine):
    Session = sessionmaker(bind=db_engine, future=True)
    s = Session()
    yield s
    s.close()

def test_insert_and_read(db_session):
    inc = CalculationCreate(a=10.0, b=2.0, type=CalculationType.DIVIDE)
    calc = create_calculation(db_session, inc)
    assert calc.result == 5.0
    loaded = get_calculation(db_session, calc.id)
    assert loaded is not None
    assert loaded.result == 5.0

def test_invalid_type_error(db_session):
    with pytest.raises(Exception):
        CalculationCreate(a=1, b=2, type="NotAType")

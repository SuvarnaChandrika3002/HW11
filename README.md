# Calculation Service (module)

## What this provides
- SQLAlchemy Calculation model
- Pydantic validation (CalculationCreate & CalculationRead)
- Calculation factory for Add/Sub/Multiply/Divide
- Unit and integration tests
- GitHub Actions CI with PostgreSQL service
- Dockerfile for building image and running tests

## Quick local setup
1. Clone repo and create venv:
```bash
git clone <your-repo-url>
cd calculation_service
python -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt

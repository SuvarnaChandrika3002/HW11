

# Calculation Model, Validation, Factory Pattern & CI/CD Pipeline

This project implements a **Calculation** model using **SQLAlchemy**, **Pydantic validation schemas**, a **factory pattern**, **unit + integration tests**, and a full **CI/CD pipeline** using GitHub Actions with PostgreSQL and Docker Hub deployment.

###  SQLAlchemy Calculation Model

Fields included:

* `id`
* `a`
* `b`
* `type` (Enum: Add, Sub, Multiply, Divide)
* `result` (computed using factory)
* Optional `user_id` foreign key support (commented in model)

###  Pydantic Schemas

* **CalculationCreate**

  * Validates `a`, `b`, and `type`
  * Prevents divide-by-zero
* **CalculationRead**

  * ORM-compatible output schema

###  Factory Pattern

Handles computing:

* Addition
* Subtraction
* Multiplication
* Division
* Raises `CalculationError` for invalid operation types

### CRUD Operations

* Create a calculation
* Fetch by ID
* Automatically compute and store `result`

### Testing (Unit + Integration)

* Unit tests for:

  * Factory logic
  * Schema validation
* Integration tests for:

  * Real PostgreSQL DB
  * CRUD behavior
  * SQLAlchemy model integrity

###  CI/CD Pipeline

GitHub Actions pipeline includes:

* PostgreSQL service
* Test execution
* Docker build
* Docker Hub push (on `main`)


## 1. Clone and set up virtual environment

```bash
git clone https://github.com/<your-username>/HW11.git
cd HW11

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Running Tests

## Unit tests

```bash
pytest tests/unit -q
```

## Integration Tests (SQLite / default)

```bash
pytest tests/integration -q
```

##  Integration Tests using PostgreSQL (Docker)

Start PostgreSQL:

```bash
docker-compose up -d
```

Set environment variable:

### Windows PowerShell:

```bash
$env:DATABASE_URL="postgresql+psycopg2://test:test@127.0.0.1:5432/testdb"
```

### macOS/Linux:

```bash
export DATABASE_URL=postgresql+psycopg2://test:test@127.0.0.1:5432/testdb
```

Run full test suite:

```bash
pytest -q
```

---

#  Docker Instructions

## Build image

```bash
docker build -t hw11:latest .
```

## Run container

```bash
docker run -it hw11:latest
```

(Currently runs tests; FastAPI endpoints come in Module 12.)

---

#  CI/CD Pipeline (GitHub Actions)

Your pipeline:

1. Checks out repo
2. Installs dependencies
3. Starts PostgreSQL service
4. Runs unit + integration tests
5. If branch is `main`:

   * Builds Docker image
   * Pushes to Docker Hub

Workflow file:
`/.github/workflows/ci.yml`

#  Docker Hub Repository

Your Docker image is automatically pushed after CI success.






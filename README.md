# RecargaYa S.A.S

## Ejecutar tests unitarios (TDD)
pytest


## Ejecutar pruebas BDD
$env:PYTHONPATH="src"
behave


## Ejecutar API FastAPI
uvicorn recargaya.api:app --reload


## Ejecutar pruebas de carga (Locust)
locust


## Ejecutar análisis de seguridad
bandit -r src


## Ejecutar pipeline CI/CD
Se ejecuta automáticamente en GitHub Actions al hacer push a la rama main
.PHONY: help venv install clean docker-up docker-down docker-build

PYTHON=python
VENV=.venv

help:
	@echo "Available commands:"
	@echo "  make venv          Activate existing virtual environment"
	@echo "  make install       Install dependencies from requirements.txt"
	@echo "  make clean         Remove virtual environment"
	@echo "  make docker-build  Build Docker images"
	@echo "  make docker-up     Start Docker services"
	@echo "  make docker-down   Stop Docker services"

venv:
	venv\Scripts\activate

run-main:
	uvicorn app.main:app --reload

install:
	pip install -r requirements.txt

clean:
	rm -rf $(VENV)

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down
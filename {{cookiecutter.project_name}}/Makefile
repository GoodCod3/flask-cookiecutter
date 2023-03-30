PYTHON=python


test:
	poetry run ${PYTHON} -m unittest discover code/ "test_*.py"

lint:
	poetry run flake8

isort:
	poetry run  isort . --check-only

isort-fix:
	poetry run  isort .

pre-commit:
	pre-commit run --all-files

freeze-dependencies:
	poetry export -f requirements.txt --output code/requirements.txt --without-hashes

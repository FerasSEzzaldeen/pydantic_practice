test:
	pytest --cov-fail-under=100 --cov=src tests
lint: 
	flake8 src
	mypy src
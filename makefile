test:
	pytest --cov-fail-under=100 --cov=src tests
lint: 
	flake8 src
	mypy src

setup:
	docker-compose run transformation

insert:
	docker-compose run transformation python -m aws.make_queue

read:
	docker-compose run transformation python -m aws.read_queue

check:
	docker-compose run transformation python -m aws.last_check
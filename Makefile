build:
	docker-compose build

down:
	docker-compose down --remove-orphans

run:
	docker-compose run app python script.py

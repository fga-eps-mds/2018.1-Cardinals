CONTAINER_NAME ?= cardinalsweb

build:
	# Build or rebuild services
	docker-compose build

up:
	# Create and start containers
	docker-compose up

upd:
	# Create and start containers in the background
	docker-compose up -d

stop:
	# Stop running containers without removing them
	docker-compose stop

down:
	# Stop and remove containers
	docker-compose down
ps:
	# List containers
	docker ps

log:
	# View output from containers
	docker-compose logs

shell:
	# Execute the bash of the main container
	docker exec -it $(CONTAINER_NAME) bash

updatershell:
	# Execute the bash of the main container
	docker exec -it updater bash

dbshell:
	docker exec -it db psql -U cardinals -W cardinals

test:
	# Execute the tests
	docker-compose -f docker-compose.test.yml run --rm web

analyze-flake8:
	# Run static analysis
	docker-compose run --rm web ./run_analysis.sh

analyze:
	# Run the Codeclimate's static analysis locally
	[ ! -z $(docker images -q codeclimate/codeclimate) ] || docker run --interactive --tty --rm   --env CODECLIMATE_CODE="$PWD"   --volume "$PWD":/code   --volume /var/run/docker.sock:/var/run/docker.sock   --volume /tmp/cc:/tmp/cc   codeclimate/codeclimate help
	CONTAINER_TIMEOUT_SECONDS=1800 codeclimate analyze

analyze-style:
	# Run the Codeclimate's style analysis locally. Checks for Python code style issues.
	[ ! -z $(docker images -q codeclimate/codeclimate-pep8) ] || docker pull codeclimate/codeclimate-pep8
	codeclimate analyze -e pep8

analyze-complexity:
	# Run the Codeclimate's complexity analysis locally
	[ ! -z $(docker images -q codeclimate/codeclimate-radon) ] || docker pull codeclimate/codeclimate-radon
	codeclimate analyze -e radon

analyze-sonar:
	# Run the Codeclimate's style analysis locally. Checks for clarity, complexity, duplication and others issues.
	[ ! -z $(docker images -q codeclimate/codeclimate-sonar-python) ] || docker pull codeclimate/codeclimate-sonar-python
	codeclimate analyze -e sonar-python

analyze-duplication:
	# Run the Codeclimate's duplication analysis locally. Checks for similar code blocks issues.
	[ ! -z $(docker images -q codeclimate/codeclimate-duplication) ] || docker pull codeclimate/codeclimate-duplication
	codeclimate analyze -e duplication

analyze-structure:
	# Run the Codeclimate's structure analysis locally. Checks for structural issues.
	[ ! -z $(docker images -q codeclimate/codeclimate-structure) ] || docker pull codeclimate/codeclimate-structure
	codeclimate analyze -e structure

default: build

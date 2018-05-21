CONTAINER_NAME ?= cardinalsweb

build: 
	docker-compose build

up:
	docker-compose up -d
	
log:
	docker-compose logs
	
shell:
	docker exec -it $(CONTAINER_NAME) bash
	
test:
	docker exec -it $(CONTAINER_NAME) ./run_tests.sh
	
analyze-flake8:
	./run_analysis.sh
	
analyze:
	[ ! -z $(docker images -q codeclimate/codeclimate) ] || docker run --interactive --tty --rm   --env CODECLIMATE_CODE="$PWD"   --volume "$PWD":/code   --volume /var/run/docker.sock:/var/run/docker.sock   --volume /tmp/cc:/tmp/cc   codeclimate/codeclimate help
	CONTAINER_TIMEOUT_SECONDS=1800 codeclimate analyze

analyze-style: 
	[ ! -z $(docker images -q codeclimate/codeclimate-pep8) ] || docker pull codeclimate/codeclimate-pep8
	codeclimate analyze -e pep8

analyze-complexity:
	[ ! -z $(docker images -q codeclimate/codeclimate-radon) ] || docker pull codeclimate/codeclimate-radon
	codeclimate analyze -e radon
	
analyze-sonar:
	[ ! -z $(docker images -q codeclimate/codeclimate-sonar-python) ] || docker pull codeclimate/codeclimate-sonar-python
	codeclimate analyze -e sonar-python

analyze-duplication:
	[ ! -z $(docker images -q codeclimate/codeclimate-duplication) ] || docker pull codeclimate/codeclimate-duplication
	codeclimate analyze -e duplication
	
analyze-structure:
	[ ! -z $(docker images -q codeclimate/codeclimate-structure) ] || docker pull codeclimate/codeclimate-structure
	codeclimate analyze -e structure

default: build

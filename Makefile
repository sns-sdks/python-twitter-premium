all: help clean lint test build

.PHONY: all

help:
	@echo "  clean       remove unwanted stuff"
	@echo "  docs        build documentation"
	@echo "  lint        check style with black"
	@echo "  test        run tests"


clean:
	rm -fr build
	rm -fr dist
	rm -fr  *.egg-info
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

docs:
	$(MAKE) -C docs html

lint:
	flake8
	black --check .


test:
	pytest -s

build: clean
	poetry build

.PHONY: docs
init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt
test:
	detox
ci:
	pytest --cov-report=xml --cov=utils/


.PHONY: docs
init:
	pip install -e .[socks]
test:
	detox
ci:
	pytest --cov-report=xml --cov=utils/


.PHONY: docs
init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt
	brownie compile
test:
	detox
ci:
	pytest --cov-report=xml --cov-config=.coveragerc --cov=badger_utils/


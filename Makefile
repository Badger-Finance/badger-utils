.PHONY: docs
init:
	pip install -e .[socks]
test:
	detox
ci:
	pytest tests --junitxml=report.xml

coverage:
	pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

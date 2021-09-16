.PHONY: docs
init:
	pip install -e .[socks]
test:
	detox
ci:
	pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=utils tests --junitxml=report.xml


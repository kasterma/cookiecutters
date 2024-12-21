all: test format scan

.PHONY: test
test:
	poetry run pytest

.PHONY: format
format:
	poetry run black *.py

.PHONY: scan
scan:
	poetry run safety check
	poetry run bandit *.py  # Note: will warn for asserts in tests

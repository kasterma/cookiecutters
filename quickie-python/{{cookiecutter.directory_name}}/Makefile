VENV=source venv/bin/activate

.PHONY: venv
venv:
	python3.8 -m venv venv
	${VENV} ; pip install -i http://localhost:8989/root/pypi/+simple/ --upgrade pip
	${VENV} ; pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv

.PHONY: test
test:
	${VENV} ; pytest

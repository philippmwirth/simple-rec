.DEFAULT_GOAL := dist

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

dist: clean 
	python3 setup.py sdist bdist_wheel
	ls -l dist

lint:
	flake8

release:
	python3 -m twine upload dist/*
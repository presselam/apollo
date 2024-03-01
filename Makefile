SOURCES := src/*.py
PYCS := $(PY_FILES:.py=.pyc)

.DEFAULT_GOAL : build

.PHONY : env build install

Pipfile.lock : Pipfile
	pipenv install --dev

dist/apollo: Pipfile.lock $(SOURCES)
	pipenv run pyinstaller --onefile --name apollo src/main.py

build : dist/apollo	$(SOURCES)

install : build
	install -m 555 dist/apollo $(HOME)/bin

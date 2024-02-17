SOURCES := src/*.py
PYCS := $(PY_FILES:.py=.pyc)


.PHONY : env build

env:
	pipenv install --dev

dist/apollo: $(SOURCES)
	pipenv run pyinstaller --onefile --name apollo src/main.py

build : dist/apollo	$(SOURCES)

install : build
	install -m 555 dist/apollo $(HOME)/bin

PYV=$(shell python -c "import sys;t='{v[0]}.{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)");

defoult: run

clean:
	rm parser.out parsetab.py

run_file:
	python3 main.py -m -l -f $(FILE)

run:
	python3 main.py -m -l

help:
	python3 main.py -h

install:
	$(PV) install ply

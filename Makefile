all: clean
	pelican posts -o public -s settings.py

clean:
	mkdir -p public
	find public -mindepth 1 -delete

run:
	cd public && python -m SimpleHTTPServer

.PHONY: all clean run

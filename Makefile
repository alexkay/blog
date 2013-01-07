all: clean
	pelican posts -o public -s settings.py
	rm -fr public/author
	rm -fr public/categories.html
	rm -fr public/category
	rm -fr public/feeds

clean:
	mkdir -p public
	find public -mindepth 1 -delete

run:
	cd public && python -m SimpleHTTPServer

.PHONY: all clean run

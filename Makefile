all: clean
	pelican posts -o public -s settings.py
	rm -fr public/author
	rm -fr public/categories.html
	rm -fr public/category
	rm -fr public/feeds

clean:
	mkdir -p public
	find public -mindepth 1 -delete

upload:
	rsync -avhzS --delete public nginx.conf server:blog

.PHONY: all clean upload

# Blog

Source code for my blog, written in Markdown and generated with [Pelican][].

## Setting up

    % virtualenv env
    % source env/bin/activate
    % pip install pelican==3.2.2 markdown
    % make

Edit the main `nginx.conf`:

    http {
        ...
        include /path/to/blog/nginx.dev.conf;
    }

Update the project location in `blog/nginx.dev.conf` and restart nginx.

Add this line to your `/etc/hosts`:

    127.0.0.1  blog.dev

Go to <http://blog.dev/>. If static files don't load make sure nginx has rx
permissions for the `blog/public` directory.

## Licence

Blog posts: cc-by-sa, code: cc0.

  [Pelican]: http://getpelican.com

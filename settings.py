#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import datetime

AUTHOR = u'Alexander Kojevnikov'
SITENAME = u'Alexander Kojevnikov | Blog'
SITEURL = 'http://kojevnikov.com'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'blog.xml'
TAG_FEED_ATOM = '%s.xml'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'en'
TIMEZONE = 'UTC'
THEME = 'theme'

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Subscribe', '/blog.xml'),
)

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

YEAR = datetime.datetime.utcnow().year

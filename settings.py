#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import datetime
import pelican

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
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
FILES_TO_COPY = (
    ('favicon.ico', 'favicon.ico'),
    ('cv.html', 'cv.html'),
    ('cv.pdf', 'cv.pdf'),
)
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Subscribe', '/blog.xml'),
)

DEFAULT_PAGINATION = 10

# Uncomment when debugging on a dev box.
# RELATIVE_URLS = True

YEAR = datetime.datetime.utcnow().year
GA_ACCOUNT = 'UA-25837667-1'

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'toc',
    'plugins.superscript',
    'plugins.subscript',
]

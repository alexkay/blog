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
FILES_TO_COPY = (
    ('favicon.ico', 'favicon.ico'),
)
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Subscribe', '/blog.xml'),
)

DEFAULT_PAGINATION = 10

YEAR = datetime.datetime.utcnow().year

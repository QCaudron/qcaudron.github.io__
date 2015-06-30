#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Quentin CAUDRON'
SITENAME = u'Quentin CAUDRON'
SITEURL = 'http://quentincaudron.com/'

PATH = 'content'

#TIMEZONE = 'USA/Princeton'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
	('github', 'https://github.com/qcaudron'),
	("twitter", "http://twitter.com/QuentinCaudron"),
	("linkedin", "https://www.linkedin.com/profile/view?id=129144766"),
	("skype", "skype:quentin.caudron"),
	("file-text-o", "http://qcaudron.github.io/files/QCaudron_CV.pdf"),
	("envelope-o", "mailto:quentincaudron@gmail.com")
)

DEFAULT_PAGINATION = 10


THEME = ("./themes/pure-single/")
COVER_IMG_URL = "./images/sea.jpg"
PROFILE_IMG_URL = "./images/q2.jpg"
TAGLINE = ("Physicist, computer scientist, accidental biologist")

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
TYPOGRIFY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

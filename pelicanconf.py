#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

# Author
AUTHOR = 'Francis G. Lee'
SITENAME = 'Francis G. Lee'
SITEURL = 'francisglee.github.io'
AUTHOR_DESCRIPTION = u'Computational Biologist, Synthetic Biologist, Software Engineer.'
AUTHOR_INTRO = u'Hi I’m Francis! Welcome to my small corner of the internet.'
AUTHOR_AVATAR = 'https://scontent.fbed1-2.fna.fbcdn.net/v/t1.0-9/943921_1038927846146417_5401770954356751244_n.jpg?_nc_cat=0&oh=37670c01fdadc020931183c0583aab04&oe=5B93DF33'
AUTHOR_WEB = 'http://francisglee.com'

# Site Settings
PATH = 'content'
TIMEZONE = 'America/New_York'
MARKUP = ('md', 'ipynb')
DEFAULT_LANG = 'en'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Theme
THEME = 'themes/minimalxy'
# MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = './content/images/favicon.ico'
MINIMALXY_START_YEAR = 2017
MINIMALXY_CURRENT_YEAR = date.today().year

# Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Services
# GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'Francis G. Lee'

# Social
SOCIAL = (
    ('facebook', 'http://www.facebook.com/ifrancium'),
    ('twitter', 'http://twitter.com/1francium'),
    ('github', 'https://github.com/francisglee'),
    ('linkedin', 'http://www.linkedin.com/in/francisglee'),
    ('instagram', 'https://www.instagram.com/francis.g.lee/'),
)


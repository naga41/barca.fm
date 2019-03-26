#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'naga41'
SITENAME = 'barca.fm'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja_JP'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Anchor', 'https://anchor.fm/barcafm'),
    ('Apple Podcasts', 'https://itunes.apple.com/us/podcast/barca-fm/id1456396781'),  # noqa: E501
    ('Google Podcasts', 'https://www.google.com/podcasts?feed=aHR0cHM6Ly9hbmNob3IuZm0vcy85YmE1ZWM0L3BvZGNhc3QvcnNz'),  # noqa: E501
    ('Spotify', 'https://open.spotify.com/show/1mQFwZhuNUK5cawwgc8opB'),
    ('Overcast', 'https://overcast.fm/itunes1456396781/barca-fm'),
    ('Pocket Casts', 'https://pca.st/mk89'),
)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-clean-blog'
SITESUBTITLE = 'バルサ好きの二人によるFCバルセロナについてのゆるトーク'
SHOW_FULL_ARTICLE = False
HEADER_COVER = 'images/camp_nou_main.jpg'
FAVICON = 'images/favicon.ico'

# set slug source filename
SLUGIFY_SOURCE = 'basename'
# set article's url only slug
ARTICLE_URL = '{slug}'

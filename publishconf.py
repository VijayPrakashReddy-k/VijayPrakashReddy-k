#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.vijayprakashk.com/'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False
# USE_LESS = False

# Delete the output directory, before generating new files
DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = "UA-176931813-1"

DISQUS_SITENAME = 'extensive-vision-ai'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

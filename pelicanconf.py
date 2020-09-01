from __future__ import unicode_literals

from datetime import datetime

AUTHOR = 'Vijayprakash'
SITETITLE = 'Vijay Prakash'
SITENAME = "Vijay Prakash"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'
SUMMARY_MAX_LENGTH = 70
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
COPYRIGHT_YEAR = datetime.today().year

PROFILE_IMG_URL = 'https://user-images.githubusercontent.com/42317258/91530727-3c21cb00-e929-11ea-9691-21088dd85801.png'
DISPLAY_TAGS_ON_SIDEBAR=True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'extensive-vision-ai'

# Blogroll
LINKS = (("The School of AI", "https://theschoolof.ai/"),
	 ("Code reference","https://github.com/VijayPrakashReddy-k/Extensive-Vision-AI/tree/master/Phase%202"),)

# Social widget
SOCIAL = (("github", "https://github.com/VijayPrakashReddy-k"),
	  ("twitter","https://twitter.com/K_VijayPrakash"),
	  ("linkdin","https://www.linkedin.com/in/vijayprakash-reddy-kovuru-ab3740166/"),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/home/vijay/projects/Extensive-vision-ai/themes/striped"
PLUGIN_PATHS = ['/home/vijay/projects/Extensive-vision-ai/plugins']
PLUGINS = ["neighbors","tag_cloud"]

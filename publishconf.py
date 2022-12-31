"""Used if `make publish` or explicitly specified as config file."""
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: E402,F403,F401

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://paw-lu.github.io"
# RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

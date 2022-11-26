"""Used if `make publish` or explicitly specified as config file."""
import os
import sys

sys.path.append(os.curdir)
import pelicanconf  # noqa: E402

# If your site is available via HTTPS, make sure SITEURL begins with https://
pelicanconf.SITEURL = "http://paw-lu.github.io"
# pelicanconf.RELATIVE_URLS = False

pelicanconf.FEED_ALL_ATOM = "feeds/all.atom.xml"
pelicanconf.CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# pelicanconf.DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

"""Used if `make publish` or explicitly specified as config file."""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://paw-lu.github.io"

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

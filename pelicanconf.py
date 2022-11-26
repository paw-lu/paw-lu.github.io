"""Configuration for Pelican."""
AUTHOR = "Paulo S. Costa"
SITENAME = "Paulo S. Costa"
SITEURL = ""

PATH = "content"

TIMEZONE = "US/Pacific"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM: str | None = None
CATEGORY_FEED_ATOM: str | None = None
TRANSLATION_FEED_ATOM: str | None = None
AUTHOR_FEED_ATOM: str | None = None
AUTHOR_FEED_RSS: str | None = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

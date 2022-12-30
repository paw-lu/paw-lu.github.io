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

DISPLAY_PAGES_ON_MENU = True
THEME = "theme"
TAILWIND = {
    "version": "3.2.4",
    "plugins": [
        "@tailwindcss/typography@0.5.8",
    ],
}

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

STATIC_PATHS = [
    "images",
    "favicons",
]
EXTRA_PATH_METADATA = {
    "favicons/favicon.ico": {"path": "favicon.ico"},
    "favicons/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "favicons/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "favicons/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "favicons/site.webmanifest": {"path": "site.webmanifest"},
    "favicons/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

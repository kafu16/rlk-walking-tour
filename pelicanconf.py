# Pelican configuration — LOCAL PREVIEW.
#
# Build:    pelican content
# Preview:  pelican --listen --bind 0.0.0.0 --port 8000
#
# For the published build see publishconf.py, which imports this file and
# overrides SITEURL / RELATIVE_URLS. Never edit URLs by hand in the content:
# use Pelican's {filename} and {static} syntax and both builds stay correct.

AUTHOR = "Reiner Lemoine Kolleg"
SITENAME = "RLK Walking Tour"
SITESUBTITLE = "Wie die Energiewende in unsere Stadt kommt"

# Empty SITEURL + RELATIVE_URLS makes every link document-relative, so the
# local preview works without knowing the final GitHub Pages subpath.
SITEURL = ""
RELATIVE_URLS = True

PATH = "content"
OUTPUT_PATH = "docs"          # GitHub Pages serves main -> /docs
THEME = "themes/rlk"

DEFAULT_LANG = "de"
TIMEZONE = "Europe/Berlin"
# No LOCALE: nothing on this site formats a date, and de_DE.UTF-8 is not
# generated in the container, so setting it only produces a build warning.

# --- content model ---------------------------------------------------------
# Every page is a station (or the home page). No articles, no blog: pages need
# no date, which is what "zeitlos" requires.
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = []

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# No archives / categories / tags / authors pages. The home page is an
# ordinary page carrying `save_as: index.html`, so Pelican must not also try
# to generate an index.html of its own.
DIRECT_TEMPLATES = []

# --- static files ----------------------------------------------------------
STATIC_PATHS = ["images", "fonts", "extra"]

# GitHub Pages runs Jekyll over the published directory unless .nojekyll is
# present, and Jekyll drops paths beginning with an underscore. Shipping it as
# a static file regenerates it on every build, so DELETE_OUTPUT_DIRECTORY
# cannot strip it.
EXTRA_PATH_METADATA = {
    "extra/nojekyll": {"path": ".nojekyll"},
}

# --- switched off ----------------------------------------------------------
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Rebuild from scratch each time, but keep .nojekyll if it ever lands here by
# another route.
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".nojekyll"]

# --- markdown --------------------------------------------------------------
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # Lets a block-level HTML element opt back into Markdown processing
        # via markdown="1" — used by the callout boxes.
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.sane_lists": {},
    },
    "output_format": "html5",
}

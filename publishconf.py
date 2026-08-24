# Pelican configuration — PUBLISHED BUILD.
#
#   pelican content -s publishconf.py
#
# Then commit docs/ and push. GitHub Pages is configured as
# "Deploy from a branch" -> main -> /docs.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

# The repo is not named <account>.github.io, so Pages serves it from a
# subpath. Setting SITEURL here (and turning relative URLs off) is what puts
# the /rlk-walking-tour prefix on every generated link. Renaming the repo
# means changing this one line.
SITEURL = "https://kafu16.github.io/rlk-walking-tour"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".nojekyll"]

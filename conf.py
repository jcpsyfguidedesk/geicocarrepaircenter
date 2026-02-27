# -----------------------------------------------------
# Path Setup
# -----------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -----------------------------------------------------
# Project Information
# -----------------------------------------------------

project = "Understanding the Geico Car Repair Process"
author = "Independent Auto Insurance Resource Center"
copyright = "2026, Independent Auto Insurance Resource Center"
release = "1.0"

# -----------------------------------------------------
# General Configuration
# -----------------------------------------------------

extensions = [
    "sphinx.ext.githubpages",     # Production deployment
    "sphinx.ext.autosectionlabel" # Clean internal linking
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "en"

# Prevent duplicate section warnings
autosectionlabel_prefix_document = True

# -----------------------------------------------------
# HTML Output
# -----------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_title = "Geico Car Repair Information | Insurance Claim Process Guide"
html_static_path = ["_static"]

html_css_files = [
    "custom.css",
]

html_theme_options = {
    "navbar_align": "left",
    "navigation_depth": 3,
    "show_prev_next": False,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field"],
    "footer_start": ["copyright"],
    "footer_center": [],
    "footer_end": [],
}

# Logo (optional but recommended)
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

# -----------------------------------------------------
# Clean Output Settings
# -----------------------------------------------------

html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

# -----------------------------------------------------
# Sidebar Configuration
# -----------------------------------------------------

html_sidebars = {
    "**": ["sidebar-nav-bs.html"]
}

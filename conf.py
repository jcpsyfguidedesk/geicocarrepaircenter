# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Understanding the Geico Car Repair Process'
author = 'Independent Auto Insurance Resource Center'
copyright = '2026, Independent Auto Insurance Resource Center'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.githubpages',   # for production deployment
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'en'

# -- HTML output -------------------------------------------------------------

html_theme = 'furo'   # More modern and professional than RTD

html_title = "Understanding the Geico Car Repair Process"
html_static_path = ['_static']

html_theme_options = {
    "navigation_with_keys": True,
}

# Remove unnecessary clutter
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

# -- SEO & Branding ----------------------------------------------------------

html_favicon = '_static/favicon.ico'  # optional
html_logo = '_static/logo.png'        # optional

# -- Sidebar (Clean Layout) --------------------------------------------------

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
    ]
}

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Geico Car Repair Guide'
copyright = '2026, Independent Auto Insurance Resource Center'
author = 'Independent Auto Insurance Resource Center'
release = '1.0'
version = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_title = "Geico Car Repair Guide | Insurance Claim & Repair Information"
html_short_title = "Geico Car Repair Guide"

html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False
}

# Custom CSS (optional)
html_css_files = [
    'custom.css',
]

# SEO Meta Tags
html_context = {
    "meta_description": "Independent guide explaining Geico car repair claims, vehicle damage estimates, insurance repair process, and choosing a repair shop.",
    "meta_keywords": "Geico car repair, Geico claim process, auto insurance repair, insurance estimate guide, collision repair information",
}

# -- HTML Sidebar configuration ---------------------------------------------

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Output options ----------------------------------------------------------

html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# -- LaTeX output (optional) -------------------------------------------------

latex_elements = {}

latex_documents = [
    ('index', 'GeicoCarRepairGuide.tex',
     'Geico Car Repair Guide Documentation',
     'Independent Auto Insurance Resource Center', 'manual'),
]

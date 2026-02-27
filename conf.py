# -- Project information -----------------------------------------------------

project = "Understanding the Geico Car Repair Process"
author = "Independent Auto Insurance Resource Center"
copyright = "2026, Independent Auto Insurance Resource Center"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- HTML output -------------------------------------------------------------

html_theme = 'alabaster'   # Default Sphinx theme (no installation needed)

html_title = "Geico Car Repair Information Guide"

html_static_path = ['_static']

# Clean professional output
html_show_sphinx = False
html_show_sourcelink = False

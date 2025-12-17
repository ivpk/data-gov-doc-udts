import os
import sys
from datetime import date

project = 'UDTS Sąveikos Vadovas'
copyright = f'{date.today().year}, Valstybės duomenų agentūra'
author = 'Valstybės duomenų agentūra'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',  # Leidžia naudoti Markdown
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'lt'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

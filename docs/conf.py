# -*- coding: utf-8 -*-
#

import sys
import os
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../src/'))

extensions = [
    'sphinx.ext.autodoc',
    "sphinx_rtd_theme",
    ]
source_suffix = '.rst'
master_doc = 'index'
project = u'Sphinx Autodoc Example'
copyright = u'Your Name Here'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
autoclass_content = "both"

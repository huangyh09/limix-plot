import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))


def get_version():
    import limix_plot
    return limix_plot.__version__


def get_name():
    import limix_plot
    return limix_plot.__name__


extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = get_name()
copyright = '2018, Danilo Horta'
author = 'Danilo Horta'

version = get_version()
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'conf.py']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

htmlhelp_basename = 'limix-plotdoc'

man_pages = [
    (master_doc, 'limix-plot', 'limix-plot Documentation',
     [author], 1)
]

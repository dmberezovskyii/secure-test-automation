# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'secure-test-automation'
copyright = '2025, Dmytro Berezovskyi'
author = 'Dmytro Berezovskyi'
release = '1.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []
pygments_style = "sphinx"
highlight_language = "python"

html_static_path = ['_static']
html_theme = "sphinx_rtd_theme"

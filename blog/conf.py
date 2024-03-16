# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

# -- Project information 
project = "Gil Kanfer, PhD" 
copyright = "Gil Kanfer"
author = "Gil Kanfer"
html_title = "💻🧬📊🔬💊📚"

# load extensions
extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

# specify project details
master_doc = "index"
project = "MyST-NB Quickstart"

# basic build settings
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    "README.md",
    "**/.ipynb_checkpoints/*",
    "docs",
    "temp",
]
nitpicky = True

html_sidebars = {
    "index": ["gil-kanfer-profile.html"],
    "about": ["gil-kanfer-profile.html"],
    "projects": ["gil-kanfer-profile.html"],
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
    "publications": ["gil-kanfer-profile.html"],
}

redirect_folders = {
    "posts": "blog",
}

# Add theme
html_theme = "pydata_sphinx_theme"

#file system and favicon:
html_static_path = ["_static"]
html_favicon = "_static/images/logo.ico"

# MyST
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_url_schemes = ("http", "https", "mailto")

html_theme_options = {
    "search_bar_text": "Search this site...",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/gkanfer",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/gil_kanfer",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/gil-kanfer-b8684028/",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}

templates_path = ["_templates"]
html_sidebars = {
    "index": ["gil-kanfer-profile.html"],
    "projects": ["gil-kanfer-profile.html"],
    "publications": ["gil-kanfer-profile.html"]
}

html_css_files = ["css/mycss.css"]


jupyter_execute_notebooks = "off"

blog_title = "Gil Kanfer, PhD"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Using the Bayesian Approach to Analyze Functional Genomics Screen with Pymc."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2



# Custom formats for reading notebook; suffix -> reader
# nb_custom_formats = {}

# Notebook level metadata key for config overrides
# nb_metadata_key = 'mystnb'

# Cell level metadata key for config overrides
# nb_cell_metadata_key = 'mystnb'

# Mapping of kernel name regex to replacement kernel name(applied before execution)
# nb_kernel_rgx_aliases = {}

# Execution mode for notebooks
# nb_execution_mode = 'auto'

# Path to folder for caching notebooks (default: <outdir>)
# nb_execution_cache_path = ''

# Exclude (POSIX) glob patterns for notebooks
# nb_execution_excludepatterns = ()

# Execution timeout (seconds)
# nb_execution_timeout = 30

# Use temporary folder for the execution current working directory
# nb_execution_in_temp = False

# Allow errors during execution
# nb_execution_allow_errors = False

# Raise an exception on failed execution, rather than emitting a warning
# nb_execution_raise_on_error = False

# Print traceback to stderr on execution error
# nb_execution_show_tb = False

# Merge stdout/stderr execution output streams
# nb_merge_streams = False

# The entry point for the execution output render class (in group `myst_nb.output_renderer`)
# nb_render_plugin = 'default'

# Remove code cell source
# nb_remove_code_source = False

# Remove code cell outputs
# nb_remove_code_outputs = False

# Prompt to expand hidden code cell {content|source|outputs}
# nb_code_prompt_show = 'Show code cell {type}'

# Prompt to collapse hidden code cell {content|source|outputs}
# nb_code_prompt_hide = 'Hide code cell {type}'

# Number code cell source lines
# nb_number_source_lines = False

# Overrides for the base render priority of mime types: list of (builder name, mime type, priority)
# nb_mime_priority_overrides = ()

# Behaviour for stderr output
# nb_output_stderr = 'show'

# Pygments lexer applied to stdout/stderr and text/plain outputs
# nb_render_text_lexer = 'myst-ansi'

# Pygments lexer applied to error/traceback outputs
# nb_render_error_lexer = 'ipythontb'

# Options for image outputs (class|alt|height|width|scale|align)
# nb_render_image_options = {}

# Options for figure outputs (classes|name|caption|caption_before)
# nb_render_figure_options = {}

# The format to use for text/markdown rendering
# nb_render_markdown_format = 'commonmark'

# Javascript to be loaded on pages containing ipywidgets
# nb_ipywidgets_js = {'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js': {'integrity': 'sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=', 'crossorigin': 'anonymous'}, 'https://cdn.jsdelivr.net/npm/@jupyter-widgets/html-manager@1.0.6/dist/embed-amd.js': {'data-jupyter-widgets-cdn': 'https://cdn.jsdelivr.net/npm/', 'crossorigin': 'anonymous'}}

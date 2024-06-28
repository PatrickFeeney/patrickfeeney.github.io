AUTHOR = 'Patrick Feeney'
SITENAME = 'Patrick Feeney'
SITEURL = ""

PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/PatrickFeeney"),
    ("Google Scholar",
     "https://scholar.google.com/citations?user=GQY8QDYAAAAJ&hl=en"),
)

# Social widget
SOCIAL = (
    ("patrickfeeney1225@gmail.com", "mailto:patrickfeeney1225@gmail.com"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelican-bootstrap3 config
THEME = "submodules/pelican-themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['submodules/pelican-plugins']
PLUGINS = ['i18n_subsites', 'pelican_cite']

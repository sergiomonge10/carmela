# Django settings for carmela project.
import os
from django.utils.translation import ugettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'carmela', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': '280690', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''
MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3r+jt2nf^3a4lt44sik4t4t@lg-s0u*w(zjo1x1=y&amp;v-rupd^%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'carmela.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'carmela.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (

"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request"

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'multimedia',
    'noticias',
    'paginas',
    'uniffut',
    'tinymce',

    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

# Configuracion de DASHBOARD-FLUENT-ADMIN
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'
# ADMIN_MEDIA_PREFIX = '/static/admin/'

FLUENT_DASHBOARD_DEFAULT_MODULE = 'admin_tools.dashboard.modules.AppList'
FLUENT_DASHBOARD_ICON_THEME = 'oxygen'

FLUENT_DASHBOARD_APP_ICONS = {
    'multimedia/patrocinador': 'preferences-contact-list.png',
    'multimedia/multimedia': 'view-media-visualization.png',
    'paginas/pagina': 'folder-txt.png',
    'paginas/tablaprimera': 'view-conversation-balloon.png',
    'paginas/tablasegunda': 'folder.png',
    'noticias/noticia': 'view-pim-news.png',
    'multimedia/categoriamultimedia': 'view-choose.png',
    'multimedia/tipomultimedia': 'view-multiple-objects.png',
    'uniffut/bitacora': 'view-pim-tasks.png',
    'uniffut/division': 'server-database.png',
    'uniffut/equipo': 'view-calendar-list.png',
    'uniffut/jugador': 'view-media-playlist.png',
    'uniffut/torneo': 'view-calendar-journal.png',
    'he_one/host': 'preferences-desktop-wallpaper.png',
    'he_one/pcfile': 'folder-remote.png',
    'he_one/log': 'utilities-system-monitor.png',
    'he_one/namesystem': 'server-database.png',
    'he_one/filepermission': 'kwalletmanager.png',
    'he_one/userpermission': 'resource-group.png',
}

FLUENT_DASHBOARD_APP_GROUPS = (
    ('Multimedia', {
        'models': (
            'multimedia.models.*',
        ),
    }),
    ('Noticias', {
        'models': (
            'noticias.models.*',
        ),
    }),
    ('Paginas', {
        'models': (
            'paginas.models.*',
        ),
    }),
    ('Uniffut', {
        'models': (
            'uniffut.models.*',
        ),
    }),
    ('Administration', {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            'registration.*',
        ),
    }),
    ('Applications', {
        'models': ('*',),
        'module': 'AppList',
        'collapsible': True,
    }),
)



# Configuracion del TINYMCE
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

TINYMCE_SPELLCHECKER = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

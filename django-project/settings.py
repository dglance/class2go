# Django settings for class2go project.

from database import *
from os import path
#ADDED FOR url tag future
import django.template
django.template.add_to_builtins('django.templatetags.future')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# If you upload files from a dev machine, set MEDIA_ROOT to be the root dir for the file
# uploads. If you do this, set in in database.py; not this file.
#Also, if you set it in database.py, don't uncomment the following line as settings.py
#runs after database.py
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/opt/class2go/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

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
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'


thispath = path.dirname(path.realpath(__file__))
TEMPLATE_DIRS = (
    thispath+'/templates'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages'
)

# the mode should be set in your database.py, but if it's not, assume
# we're in a dev environment (careful!)
try:
        class2go_mode
except NameError:
        class2go_mode = 'dev'


INSTALLED_APPS = (
                      'django.contrib.auth',
                      'django.contrib.contenttypes',
                      'django.contrib.sessions',
                      'django.contrib.sites',
                      'django.contrib.messages',
                      'django.contrib.staticfiles',
                      # Uncomment the next line to enable the admin:
                      'django.contrib.admin',
                      # Uncomment the next line to enable admin documentation:
                      'django.contrib.admindocs',
                      'registration',
                      'south',
                      'c2g',
                      'courses',
                      'courses.forums',
                      'courses.announcements',
                      'courses.videos',
                      'courses.video_exercises',
                      'khan',
                      'problemsets',
                      'django.contrib.flatpages',
                      'storages',
                      )
if class2go_mode != "prod":
    INSTALLED_APPS += (
                        'db_test_data',
                       )

# Storage

# By default we use S3 storage.  Make sure we have the settings we need.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
try:
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME
except NameError:
    # TODO: fail if not defined
    pass

# Setting these variables to 'local' is the idiom for using local storage.
if (AWS_ACCESS_KEY_ID == 'local' or AWS_SECRET_ACCESS_KEY == 'local' or
        AWS_STORAGE_BUCKET_NAME == 'local'):
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    # We need MEDIA_ROOT to be set to something useful in this case
    try:
        MEDIA_ROOT
    except NameError:
        # TODO: fail if not defined
        pass

#This states that app c2g's UserProfile model is the profile for this site.
AUTH_PROFILE_MODULE = 'c2g.UserProfile'

ACCOUNT_ACTIVATION_DAYS = 7 #used by registration


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

# Session Settings
SESSION_COOKIE_AGE = 3*30*24*3600

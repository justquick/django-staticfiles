from django.conf import settings

# The directory in which the static files are collected in
ROOT = getattr(settings, 'STATIC_ROOT', None)

# The URL path to STATIC_ROOT
URL = getattr(settings, 'STATIC_URL', '')

# A tuple of two-tuples with a name and the path of additional directories
# which hold static files and should be taken into account
DIRS = getattr(settings, 'STATICFILES_DIRS', ())

# Names of sub directories in apps that should be automatically scanned
MEDIA_DIRNAMES = getattr(settings, 'STATICFILES_MEDIA_DIRNAMES', ['media'])

# Apps that have media in <app>/media, not in <app>/media/<app>,
# e.g. django.contrib.admin
PREPEND_LABEL_APPS = getattr(settings, 'STATICFILES_PREPEND_LABEL_APPS',
                             ('django.contrib.admin',))

# Apps that shouldn't be taken into account when collecting app media
EXCLUDED_APPS = getattr(settings, 'STATICFILES_EXCLUDED_APPS', ())

APPS = [app for app in settings.INSTALLED_APPS if app not in EXCLUDED_APPS]

# Destination storage
STORAGE = getattr(settings, 'STATICFILES_STORAGE',
                  'staticfiles.storage.StaticFileStorage')

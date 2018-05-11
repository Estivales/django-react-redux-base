from djangoreactredux.settings.dev import *  # NOQA (ignore all errors on this line)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "DB_NAME",
        'USER': "root",
        'PASSWORD': "root",
        'HOST': "127.0.0.1",
        'PORT': "3306",
        'OPTIONS': {
            'init_command': "set GLOBAL sql_mode='NO_ENGINE_SUBSTITUTION';",
        }
    },
}

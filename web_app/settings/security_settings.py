from .operations import resolve

DEBUG = resolve('DEBUG', default=False, var_type=bool, raise_error=True)

class Time:
    SECOND = 1
    MINUTE = SECOND * 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    WEEK = DAY * 7
    YEAR = WEEK * 52
    MONTH = YEAR / 12

if not DEBUG:
    SECURE_HSTS_SECONDS = Time.MONTH
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
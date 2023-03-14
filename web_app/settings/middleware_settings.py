from .operations import resolve

DEBUG = resolve('DEBUG', default=False, var_type=bool, raise_error=True)

MIDDLEWARE_INDEX = (
    # Name,                                                              Production,  Development, Enabled,     Position
    ('django.middleware.security.SecurityMiddleware',                    True,        True,        True,        10),
    
    ('django.middleware.cache.UpdateCacheMiddleware',                    True,        True,        False,       20),
    ('django.middleware.gzip.GZipMiddleware',                            True,        True,        False,       30),
      
    ('django.contrib.sessions.middleware.SessionMiddleware',             True,        True,        True,        40),

    ('django.middleware.common.BrokenLinkEmailsMiddleware',              True,        True,        False,       50),
   
    ('django.middleware.http.ConditionalGetMiddleware',                  True,        True,        True,        60),
    ('django.middleware.locale.LocaleMiddleware',                        True,        True,        True,        70),
      
    ('django.middleware.common.CommonMiddleware',                        True,        True,        True,        80),
    ('django.middleware.csrf.CsrfViewMiddleware',                        True,        True,        True,        90),
    ('django.contrib.auth.middleware.AuthenticationMiddleware',          True,        True,        True,        100),

    ('django.contrib.auth.middleware.AuthenticationMiddleware',          True,        True,        True,        110),
    ('django.contrib.auth.middleware.RemoteUserMiddleware',              True,        True,        True,        120),
 
    ('django.contrib.messages.middleware.MessageMiddleware',             True,        True,        True,        130),
    ('django.contrib.sites.middleware.CurrentSiteMiddleware',            True,        True,        True,        140),
    ('django.middleware.clickjacking.XFrameOptionsMiddleware',           True,        True,        True,        150),

    ('django.middleware.cache.FetchFromCacheMiddleware',                 True,        True,        True,        160),
    ('django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',   True,        True,        False,       170),
    ('django.contrib.redirects.middleware.RedirectFallbackMiddleware',   True,        True,        False,       180),
                  

    ('debug_toolbar.middleware.DebugToolbarMiddleware',                  False,       True,        True,        1),
)

MIDDLEWARE = [ 
    app for app, production, development, enabled, _ in sorted(MIDDLEWARE_INDEX, key=lambda x:x[4]) 
        if (enabled and ((DEBUG is False and production == True) or (DEBUG is True and development == True))) 
    ]
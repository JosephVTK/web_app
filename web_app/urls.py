"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from .robots import RobotsView

from blog.views import ArticleViewSet
from blog.sitemaps import ArticleSitemap


urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index_page'),
    path('mymodels/', include('core_app.urls')),
    path('accounts/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('document/', include('document.urls')),
    path('admin/', admin.site.urls),
]

if settings.USE_API is True:
    router = DefaultRouter()
    router.register(r'articles', ArticleViewSet)

    urlpatterns.append(
        path('__api__/', include(router.urls))
    )

if settings.USE_SITEMAPS is True:
    urlpatterns.append(
    path('sitemap.xml', sitemap, 
    {'sitemaps': 
        { 'articles' : ArticleSitemap }
    }, name='django.contrib.sitemaps.views.sitemap')
    )

if settings.USE_ROBOTS is True:
    urlpatterns.append(
        path("robots.txt", RobotsView.as_view()),
    )

if settings.DEBUG is True:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Load the Admin File Here
import web_app.config.admin

"""channelworm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from modelcompletion.views import index


urlpatterns = [
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^index$', index),

    url(r'^pyopenworm/',
        include(('modelcompletion.urls', 'modelcompletion'), namespace="modelcompletion"),),
    url(r'^pyopenworm/api/',
        include(('modelcompletion.api.urls', 'modelcompletion-api'), namespace="modelcompletion-api"),),

    url(r'^$', index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

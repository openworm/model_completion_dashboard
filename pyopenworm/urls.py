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
from django.conf.urls import url

from views import index, Neurons, Neuron, Muscles, Muscle


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^neurons$', Neurons, name='neurons-index'),
    url(r'^neuron/(?P<neuron_id>\w+)$', Neuron, name='neuron-index'),

    url(r'^muscles$', Muscles, name='muscles-index'),
    url(r'^muscle/(?P<muscle_id>\w+)$', Muscle, name='muscle-index'),

]

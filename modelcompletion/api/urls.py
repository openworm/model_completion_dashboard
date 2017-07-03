from django.conf.urls import url

from .views import AllNeurons,CellIonChannels

urlpatterns = [
    url(r'^getneurons/$', AllNeurons.as_view(), name='getneurons'),
    url(r'^getcellionchannels/$',CellIonChannels.as_view(),name="getcellionchannels"),
]

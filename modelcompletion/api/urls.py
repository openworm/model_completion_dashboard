from django.conf.urls import url

from .views import AllNeurons,AllMuscles,CellIonChannels

urlpatterns = [
    url(r'^getneurons/$', AllNeurons.as_view(), name='getneurons'),
    url(r'^getmuscles/$', AllMuscles.as_view(), name='getmuscles'),
    url(r'^getcellionchannels/$',CellIonChannels.as_view(),name="getcellionchannels"),
]

from django.conf.urls import url

from .views import AllNeurons,AllMuscles,CellIonChannels,AllCells,BodyMuscles,PharynxMuscles,FindCell

urlpatterns = [
    url(r'^getneurons/$', AllNeurons.as_view(), name='getneurons'),
    url(r'^getmuscles/$', AllMuscles.as_view(), name='getmuscles'),
    url(r'^getcellionchannels/$',CellIonChannels.as_view(),name="getcellionchannels"),
    url(r'^getallcells/$',AllCells.as_view(),name="getallcells"),
    url(r'^getbodymuscles$',BodyMuscles.as_view(),name="getbodymuscles"),
    url(r'^getpharynxmuscles$',PharynxMuscles.as_view(),name="getpharynxmuscles"),
    url(r'^findcell$',FindCell.as_view(),name="findcell"),
]

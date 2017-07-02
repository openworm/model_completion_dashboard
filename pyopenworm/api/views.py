from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint

from .serializers import NeuronSerializer,ChannelSerializer



class Neuron(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class Channel(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class AllNeurons(APIView):

    def get(self, request, format=None):
        Neurons = [Neuron(name="Neuron(Neuron:SABD)"),Neuron(name="Neuron(Neuron:RMDDR)"),Neuron(name="Neuron(Neuron:CEPVL)")]
        serializer = NeuronSerializer(Neurons, many=True)
        print serializer.data
        return Response(serializer.data)

class CellIonChannels(APIView):

    def get(self,request, format=None):
        Channels = [Channel(name="Channel(Channel:SABD)"),Channel(name="Channel(Channel:RMDDR)"),Channel(name="Channel(Channel:CEPVL)")]
        serializer_class = ChannelSerializer
        cellname = self.request.query_params.get('cellname', None)
        if cellname==None:
            Channels=[]
        serializer = ChannelSerializer(Channels, many=True)
        print serializer.data
        return Response(serializer.data)

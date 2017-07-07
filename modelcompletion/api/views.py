from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint
import PyOpenWorm as P

from .serializers import NeuronSerializer,ChannelSerializer, MuscleSerializer



class Neuron(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class Muscle(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class Channel(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class AllNeurons(APIView):

    def get(self, request, format=None):

        Neurons = []
        try:
            for neuron in P.Neuron().load():
                    Neurons.append(Neuron(name=str(neuron)))
        finally:
            print "done"
        serializer = NeuronSerializer(Neurons, many=True)
        print serializer.data
        return Response(serializer.data)

class AllMuscles(APIView):

    def get(self, request, format=None):

        Muscles = []
        for muscle in P.Muscle().load():
            Muscles.append(Muscle(name=str(muscle)))
        print Muscles
        serializer = MuscleSerializer(Muscles, many=True)
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

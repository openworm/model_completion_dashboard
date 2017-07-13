from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint
import PyOpenWorm as P
import csv
import os
import operator
from django.conf import settings

from .serializers import NeuronSerializer,ChannelSerializer, MuscleSerializer, CellSerializer



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

class Cell(object):
    def __init__(self, name):
        self.name = name

class AllNeurons(APIView):

    def get(self, request, format=None):

        Neurons = []
        try:
            for neuron in P.Neuron().load():
                    Neurons.append(Neuron(name=str(neuron.name())))
        finally:
            print "done"
        Neurons.sort(key=operator.attrgetter('name'))
        serializer = NeuronSerializer(Neurons, many=True)
        return Response(serializer.data)

class AllMuscles(APIView):

    def get(self, request, format=None):

        Muscles = []
        try:
            for muscle in P.Muscle().load():
                Muscles.append(Muscle(name=str(muscle.name())))
        finally:
            print "done"
        serializer = MuscleSerializer(Muscles, many=True)
        return Response(serializer.data)

class BodyMuscles(APIView):

    def get(self, request, format=None):

        Bodymuscles = []
        try:
            input_file = open(os.path.join(settings.DATA_DIR,'bodywallmuscles.csv'))
            file_reader = csv.DictReader(input_file)
            for row in file_reader:
                Bodymuscles.append(Muscle(name = str(row["Body wall muscles"])))
        finally:
            print "done"

        serializer= MuscleSerializer(Bodymuscles, many=True)
        return Response(serializer.data)



class PharynxMuscles(APIView):

    def get(self, request, format=None):

        Pharynmuscles = []
        try:
            input_file = open(os.path.join(settings.DATA_DIR,'pharynxmuscles.csv'))
            file_reader = csv.DictReader(input_file)
            for row in file_reader:
                Pharynmuscles.append(Muscle(name = str(row["Pharynx muscles"])))
        finally:
            print "done"

        serializer= MuscleSerializer(Pharynmuscles, many=True)
        return Response(serializer.data)

class AllCells(APIView):

    def get(self, request, format=None):
        Cells = []
        try:
            for neuron in P.Neuron().load():
                Cells.append(Cell(name=str(neuron.name())))
            for muscle in P.Muscle().load():
                Cells.append(Cell(name=str(muscle.name())))
        finally:
            print "done"
        serializer = CellSerializer(Cells, many=True)
        return Response(serializer.data)

class CellIonChannels(APIView):

    def get(self,request, format=None):
        Channels = [Channel(name="SABD"),Channel(name="RMDDR"),Channel(name="CEPVL")]
        serializer_class = ChannelSerializer
        cellname = self.request.query_params.get('cellname', None)
        if cellname==None:
            Channels=[]
        serializer = ChannelSerializer(Channels, many=True)
        print serializer.data
        return Response(serializer.data)


class FindCell(APIView):

    def get(self,request, format=None):

        serializer_class = ChannelSerializer
        cellname = self.request.query_params.get('cellname', None)
        if cellname==None:
            Channels=[]
        serializer = ChannelSerializer(Channels, many=True)
        print serializer.data
        return Response(serializer.data)

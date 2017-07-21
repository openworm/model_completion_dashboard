from django.http import Http404
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint
import PyOpenWorm as P
import csv
import os
import operator
import json
from django.http import HttpResponse
from django.conf import settings

from .serializers import NeuronSerializer,ChannelSerializer, MuscleSerializer, CellSerializer, NeuronDetailSerializer, MuscleDetailSerializer



class Neuron(object):

    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class NeuronDetail(object):
    name= None
    completeness= None
    receptors = None
    type = None
    innexin= None
    neurotransmitter = None
    neuropeptide = None
    def __init__(self, neuron):
        self.name = neuron.name()
        self.type = neuron.type()
        self.completeness=randint(0,9)
        self.receptors = sorted(neuron.receptors())
        self.innexin = sorted(neuron.innexin())
        self.neurotransmitter = sorted(neuron.neurotransmitter())
        self.neuropeptide = sorted(neuron.neuropeptide())

class Muscle(object):
    def __init__(self, name,completeness=None):
        self.name = name
        self.completeness=randint(0,9)

class MuscleDetail(object):
    name= None
    completeness= None
    neurons= None
    receptors = None
    def __init__(self, muscle):
        self.name = muscle.name()
        self.completeness=randint(0,9)
        self.neurons = sorted(muscle.neurons())
        self.receptors = sorted(muscle.receptors())

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

        neurons=[]
        muscles=[]
        Channels = [Channel(name="SABD"),Channel(name="RMDDR"),Channel(name="CEPVL")]
        for neuron in P.Neuron().load():
            neurons.append(str(neuron.name()))
        for muscle in P.Muscle().load():
            muscles.append(str(muscle.name()))
        cellname = self.request.query_params.get('cellname', None)
        if cellname==None:
            Channels=[]
        else:
            if cellname in neurons:
                net = P.Worm().get_neuron_network()
                neuron = net.aneuron(cellname)
                serializer = NeuronDetailSerializer(NeuronDetail(neuron))
            elif cellname in muscles:
                muscle = P.Muscle(cellname)
                serializer = MuscleDetailSerializer(MuscleDetail(muscle))
        print serializer.data
        return Response(serializer.data)

class SearchSuggestion(View):

    Allcells=[]
    def __init__(self):
        self.Allcells = []
        for neuron in P.Neuron().load():
            self.Allcells.append(str(neuron.name()))
        for muscle in P.Muscle().load():
            self.Allcells.append(str(muscle.name()))

    def get(self,request, format=None):

        cellname = self.request.GET.get('term', '')
        Suggestion = []
        if cellname==None:
            Suggestion = []
        else:
            Suggestion = filter(lambda k: cellname in k, self.Allcells)

        data = json.dumps(Suggestion)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

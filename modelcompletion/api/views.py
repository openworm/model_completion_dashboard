from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from PyOpenWorm.neuron import Neuron as PNeuron
from PyOpenWorm.muscle import Muscle as PMuscle
from PyOpenWorm.channel import Channel as PChannel
from PyOpenWorm.worm import Worm as PWorm
import csv
import os
import operator
import json
from django.http import HttpResponse
from django.conf import settings
from modelcompletion.models import (Neuron as N,
                                    IonChannel as IC,
                                    Muscle as M)
from .serializers import (NeuronSerializer,
                          ChannelSerializer,
                          MuscleSerializer,
                          CellSerializer,
                          NeuronDetailSerializer,
                          MuscleDetailSerializer,
                          IonChannelSerializer,
                          ChannelDetailSerializer)




class Neuron(object):

    def __init__(self, name, completeness=None):
        self.name = name
        nob, _ = N.objects.get_or_create(name=name)
        self.completeness = nob.completion


class NeuronDetail(object):
    celltype = None
    name = None
    completeness = None
    receptors = None
    type = None
    innexin = None
    neurotransmitter = None
    neuropeptide = None

    def __init__(self, neuron):
        self.celltype = "neuron"
        self.name = neuron.name()
        self.type = neuron.type()
        self.completeness = N.objects.get(name=neuron.name()).completion
        self.receptors = sorted(neuron.receptors())
        self.innexin = sorted(neuron.innexin())
        self.neurotransmitter = sorted(neuron.neurotransmitter())
        self.neuropeptide = sorted(neuron.neuropeptide())


class ChannelDetail(object):
    name = None
    description = None
    gene_name = None
    gene_WB_ID = None
    gene_class = None
    expression_pattern = None
    neuroML_file = None

    def __init__(self, channel):
        self.celltype = "ionchannel"
        self.name = channel.name()
        self.description = channel.description()
        self.completeness = IC.objects.get(name=channel.name()).completion
        self.gene_name = channel.gene_name()
        self.gene_WB_ID = channel.gene_WB_ID()
        self.expression = channel.expression_pattern()
        # self.neuroML_file = channel.neuroML_file()


class Muscle(object):
    def __init__(self, name, completeness=None):
        self.name = name
        mob, _ = M.objects.get_or_create(name=name)
        self.completeness = mob.completion


class IonChannel(object):
    def __init__(self, name, completeness=None):
        self.name = name
        iob, _ = IC.objects.get_or_create(name=name)
        self.completeness = iob.completion


class MuscleDetail(object):
    name = None
    celltype = None
    completeness = None
    neurons = None
    receptors = None

    def __init__(self, muscle):
        self.celltype = "muscle"
        self.name = muscle.name()
        self.completeness = M.objects.get(name=muscle.name()).completion
        self.neurons = sorted(muscle.neurons())
        self.receptors = sorted(muscle.receptors())


class Channel(object):

    def __init__(self, name, completeness=None):
        self.name = name
        cob, _ = IC.objects.get_or_create(name=name)
        self.completeness = cob.completion


class Cell(object):
    def __init__(self, name):
        self.name = name


class AllNeurons(APIView):

    def get(self, request, format=None):
        Neurons = []
        try:
            for name in PNeuron().name.get():
                Neurons.append(Neuron(name=str(name)))
        finally:
            print("done")
        Neurons.sort(key=operator.attrgetter('name'))
        serializer = NeuronSerializer(Neurons, many=True)
        return Response(serializer.data)


class AllMuscles(APIView):

    def get(self, request, format=None):

        Muscles = []
        try:
            for muscle in PMuscle().load():
                Muscles.append(Muscle(name=str(muscle.name())))
        finally:
            print("done")
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
            print("done")

        serializer= MuscleSerializer(Bodymuscles, many=True)
        return Response(serializer.data)

class AllIonChannels(APIView):

    def get(self, request, format=None):

        IonChannels = []
        try:
            for channel in PChannel().load():
                IonChannels.append(IonChannel(name=str(channel.name())))
        finally:
            print("done")
        serializer = IonChannelSerializer(IonChannels, many=True)
        return Response(serializer.data)


class PharynxMuscles(APIView):

    def get(self, request, format=None):

        Pharynmuscles = []
        try:
            input_file = open(os.path.join(settings.DATA_DIR,'pharynxmuscles.csv'))
            file_reader = csv.DictReader(input_file)
            for row in file_reader:
                Pharynmuscles.append(Muscle(name = str(row["Pharynx muscles"]).upper()))
        finally:
            print("done")

        serializer= MuscleSerializer(Pharynmuscles, many=True)
        return Response(serializer.data)

class AllCells(APIView):

    def get(self, request, format=None):
        Cells = []
        try:
            for neuron in PNeuron().load():
                Cells.append(Cell(name=str(neuron.name())))
            for muscle in PMuscle().load():
                Cells.append(Cell(name=str(muscle.name())))
        finally:
            print("done")
        serializer = CellSerializer(Cells, many=True)
        return Response(serializer.data)


class CellIonChannels(APIView):

    def get(self, request, format=None):
        print("in cell channel get data set view")
        cellname = self.request.query_params.get('cellname', None)
        if cellname is None:
            Channels = []
        else:
            neurons = []
            muscles = []
            for n in PNeuron().load():
                neurons.append(n.name())
            for m in PMuscle().load():
                muscles.append(m.name())
            if cellname in neurons:
                Channels = []
                for ch in PNeuron(name=str(cellname)).channel():
                    Channels.append(Channel(name=ch.name()))
            elif cellname in muscles:
                Channels = []
                for ch in PMuscle(name=str(cellname)).channel():
                    Channels.append(Channel(name=ch.name()))
        serializer = ChannelSerializer(Channels, many=True)
        print(serializer.data)
        return Response(serializer.data)


class FindCell(APIView):

    def get(self, request, format=None):
        neurons = []
        muscles = []
        for neuron in PNeuron().load():
            neurons.append(str(neuron.name()))
        for muscle in PMuscle().load():
            muscles.append(str(muscle.name()))
        cellname = self.request.query_params.get('cellname', None)
        if cellname is not None:
            if cellname in neurons:
                net = PWorm().get_neuron_network()
                neuron = net.aneuron(cellname)
                serializer = NeuronDetailSerializer(NeuronDetail(neuron))
            elif cellname in muscles:
                muscle = PMuscle(cellname)
                serializer = MuscleDetailSerializer(MuscleDetail(muscle))
            else:
                return Response('NO_SUCH_CELL {}'.format(cellname), status=200)
        else:
                return Response('NO_CELL_GIVEN', status=200)
        print(serializer.data)
        return Response(serializer.data)


class FindChannel(APIView):

    def get(self, request, format=None):

        channels = []
        for channel in PChannel().load():
            channels.append(str(channel.name()))
        channelname = self.request.query_params.get('channelname', None)
        if channelname is not None:
            if channelname in channels:
                channel = PChannel(channelname)
                serializer = ChannelDetailSerializer(ChannelDetail(channel))
            else:
                return Response('NO_SUCH_CHANNEL {}'.format(channelname), 200)
        else:
            return Response('No channel given')
        print(serializer.data)
        return Response(serializer.data)


class SearchSuggestion(View):

    Allcells = []

    def __init__(self):
        self.Allcells = []
        for neuron in PNeuron().load():
            self.Allcells.append(str(neuron.name()))
        for muscle in PMuscle().load():
            self.Allcells.append(str(muscle.name()))

    def get(self, request, format=None):

        cellname = self.request.GET.get('term', '')
        Suggestion = []
        if cellname is None:
            Suggestion = []
        else:
            Suggestion = filter(lambda k: cellname in k, self.Allcells)

        data = json.dumps(Suggestion)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

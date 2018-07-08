from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.generic import View
from PyOpenWorm.neuron import Neuron
from PyOpenWorm.muscle import Muscle


def Landing(request):
    return render(request, 'pyopenworm/landing.html')


def index(request):
    return render(request, 'pyopenworm/landing.html')


class SearchSuggestion(View):

    Allcells = []

    def __init__(self):
        self.Allcells = []
        for neuron in Neuron().load():
            self.Allcells.append(str(neuron.name()))
        for muscle in Muscle().load():
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

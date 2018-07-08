from __future__ import absolute_import
from __future__ import print_function
from django.core.management.base import BaseCommand
import PyOpenWorm as P
from PyOpenWorm.channel import Channel
from PyOpenWorm.neuron import Neuron as PNeuron
from PyOpenWorm.muscle import Muscle as PMuscle
from modelcompletion.models import IonChannel, Neuron, Muscle


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'to calculate the completion score of the cells and the ion channels'

    def scoring_ionchannels(self):
        print('calculating ion channel completion scores')
        for ch in Channel().load():
            channel = IonChannel(name=ch.name(), completion=0)
            channel.save()
        print('done')

    def scoring_neurons(self):
        print('calculating neuron completion scores')
        score = 0
        for n in PNeuron().load():
            score = 0
            if len(n.type()) > 0:
                score += 1
            if len(n.receptor()) > 0:
                score += 1
            if len(n.innexin()) > 0:
                score += 1
            if len(n.neurotransmitter()) > 0:
                score += 1
            if len(n.neuropeptide()) > 0:
                score += 1
            if n.neighbor.count() > 0:
                score += 1
            if n.connection.count() > 0:
                score += 1
            for ch in n.channel():
                score += IonChannel.objects.get(name=str(ch.name())).completion
            score = int((float(score) / (7 + 5 * len(n.channel()))) * float(5))
            neuron = Neuron(name=n.name(), completion=score)
            neuron.save()
        print('done')

    def scoring_muscles(self):
        print('calculating muscle completion scores')
        score = 0
        for m in PMuscle().load():
            score = 0
            if len(m.neurons()) > 0:
                score += 1
            if len(m.receptors()) > 0:
                score += 1
            for ch in m.channel():
                score += IonChannel.objects.get(name=str(ch.name())).completion
            score = int((float(score) / (2 + 5 * len(m.channel()))) * float(5))
            muscle = Muscle(name=m.name(), completion=score)
            muscle.save()
        print('done')

    def Del_Neuron(self):
        Neuron.objects.all().delete()

    def Del_Muscle(self):
        Muscle.objects.all().delete()

    def Del_IonChannel(self):
        IonChannel.objects.all().delete()

    def handle(self, *args, **options):
        P.connect('.pow/pow.conf')
        print('clearing data')
        self.Del_Neuron()
        self.Del_Muscle()
        self.Del_IonChannel()
        print('done')
        print("calculating scores")
        self.scoring_ionchannels()
        self.scoring_neurons()
        self.scoring_muscles()
        P.disconnect()
        print("scores calculated")

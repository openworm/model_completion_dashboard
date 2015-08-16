from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import json

import PyOpenWorm as P

# from formtools.wizard.views import SessionWizardView


def index(request):
    return render(request, 'pyopenworm/index.html')


def Neurons(request):
    P.connect()

    neurons = list(P.Neuron().load())

    NEURON_DICT = {}
    for neuron in neurons:
        NEURON_DICT[str(neuron)] = {'name': str(neuron),
                                    'completeness': '#2B7558'}

    P.disconnect()

    return render_to_response('pyopenworm/neurons.html',
                              {'neurons': NEURON_DICT})


def Neuron(request, neuron_id):
    P.connect()

    neurons = list(P.Neuron(neuron_id).load())

    neuron_dict = {}
    for neuron in neurons:
        neuron_dict[str(neuron)] = {
            'name': str(neuron),
            'type': list(neuron.type.get()),
            'receptor': list(neuron.receptor.get()),
            'innexin': list(neuron.innexin.get()),
            'neurotransmitter': list(neuron.neurotransmitter.get()),
            'neuropeptide': list(neuron.neuropeptide.get()),
            'completeness': '#2B7558'}

    P.disconnect()

    return render_to_response('pyopenworm/neuron.html',
                              {'neuron': neuron_dict[neuron_id]})


def Muscles(request):
    P.connect()

    muscles = list(P.Muscle().load())

    MUSCLE_DICT = {}
    for muscle in muscles:
        MUSCLE_DICT[str(muscle)] = {'name': str(muscle),
                                    'completeness': '#2B7558'}

    P.disconnect()

    return render_to_response('pyopenworm/muscles.html',
                              {'muscles': MUSCLE_DICT})


def Muscle(request, muscle_id):
    P.connect()

    muscles = list(P.Muscle(muscle_id).load())

    muscle_dict = {}
    for muscle in muscles:
        '''
            'neurons': list(muscle.neurons.get()),
            'receptors': list(muscle.receptors.get()),
        '''
        muscle_dict[str(muscle)] = {'name': str(muscle),
                                    'completeness': '#2B7558'}

    P.disconnect()

    return render_to_response('pyopenworm/muscle.html',
                              {'muscle': muscle_dict[muscle_id]})

'''
class ReferenceList(ListView):
    model = Reference
    context_object_name = 'references'


class ReferenceCreate(CreateView):
    model = Reference
    form_class = ReferenceForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('pyopenworm:reference-index')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(ReferenceCreate, self).form_valid(form)


class ReferenceWizard(SessionWizardView):
    template_name = 'pyopenworm/reference_auto_create_form.html'

    def done(self, form_list, **kwargs):
        data = self.get_cleaned_data_for_step('1')
        data['username'] = self.request.user
        instance = Reference()

        for field, value in data.iteritems():
            if (field != 'ion_channels') and (field != 'cells'):
                setattr(instance, field, value)
        instance.save()
        channels = data['ion_channels']
        cells = data['cells']
        for value in channels.iterator():
            instance.ion_channels.add(value.id)
        for value in cells.iterator():
            instance.ion_channels.add(value.id)
        return redirect('/pyopenworm/reference')

    def get_form_initial(self, step):
        initial = {}
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
        return initial


class ReferenceUpdate(UpdateView):
    model = Reference
    form_class = ReferenceForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pyopenworm:reference-index')


class ReferenceDelete(DeleteView):
    model = Reference
    success_url = reverse_lazy('pyopenworm:reference-index')


class ExperimentList(ListView):
    model = Experiment
    context_object_name = 'experiments'


class ExperimentCreate(CreateView):
    model = Experiment
    fields = ['reference']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('pyopenworm:experiment-index')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(ExperimentCreate, self).form_valid(form)


class ExperimentUpdate(UpdateView):
    model = Experiment
    fields = ['reference']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pyopenworm:experiment-index')


class ExperimentDelete(DeleteView):
    model = Experiment
    success_url = reverse_lazy('pyopenworm:experiment-index')


class IonChannelList(ListView):
    model = IonChannelModel
    context_object_name = 'ion_channel_models'


class IonChannelCreate(CreateView):
    model = IonChannelModel
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('pyopenworm:ion-channel-index')


class IonChannelUpdate(UpdateView):
    model = IonChannelModel
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pyopenworm:ion-channel-index')


class IonChannelDelete(DeleteView):
    model = IonChannelModel
    success_url = reverse_lazy('pyopenworm:ion-channel-index')


class PatchClampList(ListView):
    model = PatchClamp
    context_object_name = 'patch_clamps'


class PatchClampCreate(CreateView):
    model = PatchClamp
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('pyopenworm:patch-clamp-index')


class PatchClampUpdate(UpdateView):
    model = PatchClamp
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pyopenworm:patch-clamp-index')


class PatchClampDelete(DeleteView):
    model = PatchClamp
    success_url = reverse_lazy('pyopenworm:patch-clamp-index')


class GraphList(ListView):
    model = Graph
    context_object_name = 'graphs'


class GraphCreate(CreateView):
    model = Graph
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('pyopenworm:graph-index')


class GraphUpdate(UpdateView):
    model = Graph
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pyopenworm:graph-index')


class GraphDelete(DeleteView):
    model = Graph
    success_url = reverse_lazy('pyopenworm:graph-index')


class GraphDataList(ListView):
    model = GraphData
    context_object_name = 'graph_data'

    def get_queryset(self):
        print self.kwargs
        self.graph = get_object_or_404(Graph, id=self.kwargs['graph_id'])
        return GraphData.objects.filter(graph=self.graph)


class GraphDataDelete(DeleteView):
    model = GraphData

    def get_success_url(self):
        return reverse_lazy('pyopenworm:graph-data-index', kwargs={'graph_id': self.object.graph_id})


def save_graph_data(request):
    response_data = {
        'status': 'error', 'result': 'Saving graph data has been failed'}
    print response_data
    if request.method == 'POST':
        print "is post"
        graph = get_object_or_404(Graph, pk=request.POST.get("graph_id"))
        data = GraphData(graph=graph, series_name=request.POST.get("series_name"),
                         series_data=request.POST.get("series_data"))
        data.save()
        response_data = {
            'status': 'success', 'result': 'Graph data has been saved.'}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
'''

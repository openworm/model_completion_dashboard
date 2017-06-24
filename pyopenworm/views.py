from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from random import randint
import json
from django.http import JsonResponse

import PyOpenWorm as P



# from formtools.wizard.views import SessionWizardView


def index(request):
    return render(request, 'pyopenworm/index.html')


def getCellChannel(request):
    ROWS=20
    CHANNEL_DICT = {}
    Channels =[
    "Muscle(Muscle:VM1AL)","Muscle(Muscle:DL21)","Muscle(Muscle:PM1R)","Muscle(Muscle:VM1PR)","Muscle(Muscle:DL20)","Muscle(Muscle:DR21)","Muscle(Muscle:VM1PL)",
"Muscle(Muscle:VR8)","Muscle(Muscle:VR4)","Muscle(Muscle:PM1L)","Muscle(Muscle:VR5)","Muscle(Muscle:VR6)","Muscle(Muscle:VR7)","Muscle(Muscle:VR1)",
"Muscle(Muscle:VR2)","Muscle(Muscle:VR3)","Muscle(Muscle:PM6VR)","Muscle(Muscle:DL4)","Muscle(Muscle:DL5)","Muscle(Muscle:DL6)","Muscle(Muscle:DL7)",
"Muscle(Muscle:DL1)","Muscle(Muscle:DL2)","Muscle(Muscle:DL8)","Muscle(Muscle:DL3)","Muscle(Muscle:DL9)","Muscle(Muscle:PM5DL)","Muscle(Muscle:UM1AL)",
"Muscle(Muscle:PM2R)","Muscle(Muscle:PM2L)","Muscle(Muscle:VL23)","Muscle(Muscle:VL22)","Muscle(Muscle:VL21)","Muscle(Muscle:VL20)",
"Muscle(Muscle:PM5DR)","Muscle(Muscle:UM1AR)","Muscle(Muscle:DL10)","Muscle(Muscle:DL11)","Muscle(Muscle:DL12)","Muscle(Muscle:DL13)","Muscle(Muscle:DL14)"]
    r=0
    c=0
    count=0
    for channel in Channels:
        CHANNEL_DICT[str(r)+","+str(c)] = {'name': str(channel),
                            'completeness': randint(0, 9)}
        r+=1
        if r!=0 and r%ROWS==0:
            r=0
            c+=1
    return JsonResponse(CHANNEL_DICT)

def Landing(request):
    P.connect()
    ROWS=20
    try:
        NEURON_DICT = {}
        Neurons = ["Neuron(Neuron:SABD)",
"Neuron(Neuron:RMDDR)","Neuron(Neuron:CEPVL)","Neuron(Neuron:AIYR)","Neuron(Neuron:AIYL)","Neuron(Neuron:IL1DL)","Neuron(Neuron:RMDDL)","Neuron(Neuron:AVFR)","Neuron(Neuron:SIAVR)",
"Neuron(Neuron:SIBVR)","Neuron(Neuron:IL1L)","Neuron(Neuron:SAADL)","Neuron(Neuron:VA10)","Neuron(Neuron:VA12)","Neuron(Neuron:VA11)","Neuron(Neuron:SAADR)","Neuron(Neuron:PLMR)",
"Neuron(Neuron:IL1VR)","Neuron(Neuron:ADLL)","Neuron(Neuron:SIADL)","Neuron(Neuron:AIMR)","Neuron(Neuron:SIADR)","Neuron(Neuron:DA8)","Neuron(Neuron:DA9)","Neuron(Neuron:DA6)",
"Neuron(Neuron:DA7)","Neuron(Neuron:DA4)","Neuron(Neuron:DA5)","Neuron(Neuron:DA2)","Neuron(Neuron:DA3)","Neuron(Neuron:DA1)","Neuron(Neuron:URAVR)","Neuron(Neuron:RIGR)","Neuron(Neuron:RMGR)",
"Neuron(Neuron:RMGL)","Neuron(Neuron:AVJR)","Neuron(Neuron:VB11)","Neuron(Neuron:VB10)","Neuron(Neuron:RIGL)","Neuron(Neuron:URAVL)","Neuron(Neuron:ASIR)","Neuron(Neuron:AVDL)",
"Neuron(Neuron:ASIL)","Neuron(Neuron:AVDR)","Neuron(Neuron:ADEL)","Neuron(Neuron:SMBDR)","Neuron(Neuron:SIBDL)","Neuron(Neuron:SMBDL)","Neuron(Neuron:SIBDR)","Neuron(Neuron:ADER)",
"Neuron(Neuron:SAAVR)","Neuron(Neuron:I1L)","Neuron(Neuron:ADFR)","Neuron(Neuron:M2R)","Neuron(Neuron:SDQR)","Neuron(Neuron:AWCL)","Neuron(Neuron:VA8)","Neuron(Neuron:AWCR)","Neuron(Neuron:M4)",
"Neuron(Neuron:DB2)","Neuron(Neuron:SDQL)","Neuron(Neuron:VA1)","Neuron(Neuron:VA2)","Neuron(Neuron:VA3)","Neuron(Neuron:SAAVL)","Neuron(Neuron:I1R)","Neuron(Neuron:VA7)","Neuron(Neuron:VA6)",
"Neuron(Neuron:RIH)","Neuron(Neuron:IL2DR)","Neuron(Neuron:PVQL)","Neuron(Neuron:RID)","Neuron(Neuron:AIBL)","Neuron(Neuron:RIFR)","Neuron(Neuron:RMFL)","Neuron(Neuron:PDEL)",
"Neuron(Neuron:RMFR)","Neuron(Neuron:PDER)","Neuron(Neuron:RIFL)","Neuron(Neuron:VB1)","Neuron(Neuron:IL2VL)","Neuron(Neuron:IL2VL)","Neuron(Neuron:PHAR)","Neuron(Neuron:VB3)",
"Neuron(Neuron:SIBVL)","Neuron(Neuron:PHAL)","Neuron(Neuron:SIAVL)","Neuron(Neuron:IL2VR)","Neuron(Neuron:PVDL)","Neuron(Neuron:CEPDL)","Neuron(Neuron:SMBVL)",
"Neuron(Neuron:AFDR)","Neuron(Neuron:RMDVL)","Neuron(Neuron:AFDL)","Neuron(Neuron:RMDVR)","Neuron(Neuron:AVFL)","Neuron(Neuron:SMBVR)","Neuron(Neuron:CEPDR)","Neuron(Neuron:PVDR)",
"Neuron(Neuron:SMDDR)","Neuron(Neuron:VD9)","Neuron(Neuron:VD8)","Neuron(Neuron:VD3)","Neuron(Neuron:VD2)","Neuron(Neuron:VD1)","Neuron(Neuron:DVC)","Neuron(Neuron:VD6)","Neuron(Neuron:DVA)",
"Neuron(Neuron:VD4)","Neuron(Neuron:URYDL)","Neuron(Neuron:RICR)","Neuron(Neuron:SMDDL)","Neuron(Neuron:PVR)","Neuron(Neuron:BDUL)","Neuron(Neuron:PVT)","Neuron(Neuron:NSMR)","Neuron(Neuron:HSNL)",
"Neuron(Neuron:NSML)","Neuron(Neuron:CEPVR)","Neuron(Neuron:HSNR)","Neuron(Neuron:BDUR)","Neuron(Neuron:AVEL)","Neuron(Neuron:PVM)","Neuron(Neuron:URBL)","Neuron(Neuron:AVER)","Neuron(Neuron:FLPR)",
"Neuron(Neuron:AINR)","Neuron(Neuron:URXR)","Neuron(Neuron:RIML)","Neuron(Neuron:AS11)","Neuron(Neuron:URBR)","Neuron(Neuron:RIMR)","Neuron(Neuron:PQR)","Neuron(Neuron:AINL)","Neuron(Neuron:PHBR)",
"Neuron(Neuron:URXL)","Neuron(Neuron:ALML)","Neuron(Neuron:PHBL)","Neuron(Neuron:ALMR)","Neuron(Neuron:AS10)","Neuron(Neuron:LUAR)","Neuron(Neuron:AQR)","Neuron(Neuron:CANR)","Neuron(Neuron:VA9)",
"Neuron(Neuron:ASGR)","Neuron(Neuron:IL1DR)","Neuron(Neuron:ASGL)","Neuron(Neuron:CANL)","Neuron(Neuron:LUAL)","Neuron(Neuron:VC3)","Neuron(Neuron:VC2)","Neuron(Neuron:VC1)","Neuron(Neuron:VC6)",
"Neuron(Neuron:VC4)","Neuron(Neuron:VC5)","Neuron(Neuron:IL2R)","Neuron(Neuron:ASJR)","Neuron(Neuron:AWAR)","Neuron(Neuron:ASJL)","Neuron(Neuron:AWAL)",
"Neuron(Neuron:IL2L)"]
        r=0
        c=0
        count=0
        for neuron in Neurons:
            NEURON_DICT[(r,c)] = {'name': str(neuron),
                                'completeness': randint(0, 9)}
            r+=1
            if r!=0 and r%ROWS==0:
                r=0
                c+=1

        MUSCLE_DICT = {}
        Muscles =[
        "Muscle(Muscle:VM1AL)","Muscle(Muscle:DL21)","Muscle(Muscle:PM1R)","Muscle(Muscle:VM1PR)","Muscle(Muscle:DL20)","Muscle(Muscle:DR21)","Muscle(Muscle:VM1PL)",
"Muscle(Muscle:VR8)","Muscle(Muscle:VR4)","Muscle(Muscle:PM1L)","Muscle(Muscle:VR5)","Muscle(Muscle:VR6)","Muscle(Muscle:VR7)","Muscle(Muscle:VR1)",
"Muscle(Muscle:VR2)","Muscle(Muscle:VR3)","Muscle(Muscle:PM6VR)","Muscle(Muscle:DL4)","Muscle(Muscle:DL5)","Muscle(Muscle:DL6)","Muscle(Muscle:DL7)",
"Muscle(Muscle:DL1)","Muscle(Muscle:DL2)","Muscle(Muscle:DL8)","Muscle(Muscle:DL3)","Muscle(Muscle:DL9)","Muscle(Muscle:PM5DL)","Muscle(Muscle:UM1AL)",
"Muscle(Muscle:PM2R)","Muscle(Muscle:PM2L)","Muscle(Muscle:VL23)","Muscle(Muscle:VL22)","Muscle(Muscle:VL21)","Muscle(Muscle:VL20)",
"Muscle(Muscle:PM5DR)","Muscle(Muscle:UM1AR)","Muscle(Muscle:DL10)","Muscle(Muscle:DL11)","Muscle(Muscle:DL12)","Muscle(Muscle:DL13)","Muscle(Muscle:DL14)",
"Muscle(Muscle:DL15)","Muscle(Muscle:DL16)","Muscle(Muscle:DL17)","Muscle(Muscle:DL18)","Muscle(Muscle:PM2DR)","Muscle(Muscle:PM2DL)",
"Muscle(Muscle:VR9)","Muscle(Muscle:GLRVL)","Muscle(Muscle:PM1DL)","Muscle(Muscle:PM3R)","Muscle(Muscle:DR6)","Muscle(Muscle:DR7)",
"Muscle(Muscle:DR4)","Muscle(Muscle:PM3L)","Muscle(Muscle:DR2)","Muscle(Muscle:DR3)","Muscle(Muscle:DL19)","Muscle(Muscle:PM1DR)",
"Muscle(Muscle:VR22)","Muscle(Muscle:DR8)","Muscle(Muscle:DR9)","Muscle(Muscle:VM1AR)","Muscle(Muscle:DR16)","Muscle(Muscle:PM3VL)",
"Muscle(Muscle:DR18)","Muscle(Muscle:DR19)","Muscle(Muscle:PM4L)","Muscle(Muscle:DR12)","Muscle(Muscle:DR10)","Muscle(Muscle:DR13)",
"Muscle(Muscle:PM2VL)","Muscle(Muscle:DR11)","Muscle(Muscle:PM1VR)","Muscle(Muscle:DR14)","Muscle(Muscle:DR17)","Muscle(Muscle:PM1VL)",
"Muscle(Muscle:PM2VR)"]
        for muscle in Muscles:
            MUSCLE_DICT[str(muscle)] = {'name': str(muscle),
                                        'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/landing.html',
                              {'neurons': NEURON_DICT,
                              'neuronRows': 5,
                              'neuronCols': c,
                              'muscles' : MUSCLE_DICT})


def Neurons(request):
    P.connect()

    try:
        NEURON_DICT = {}
        for neuron in P.Neuron().load():
            NEURON_DICT[str(neuron)] = {'name': str(neuron),
                                        'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/neurons.html',
                              {'neurons': NEURON_DICT})


def Neuron(request, neuron_id):
    P.connect()

    try:
        neuron_dict = {}
        for neuron in P.Neuron(neuron_id).load():
            neuron_dict[str(neuron)] = {
                'name': str(neuron),
                'type': list(neuron.type.get()),
                'receptor': list(neuron.receptor.get()),
                'innexin': list(neuron.innexin.get()),
                'neurotransmitter': list(neuron.neurotransmitter.get()),
                'neuropeptide': list(neuron.neuropeptide.get()),
                'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/neuron.html',
                              {'neuron': neuron_dict[neuron_id]})


def Muscles(request):
    P.connect()

    try:
        MUSCLE_DICT = {}
        for muscle in P.Muscle().load():
            MUSCLE_DICT[str(muscle)] = {'name': str(muscle),
                                        'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/muscles.html',
                              {'muscles': MUSCLE_DICT})


def Muscle(request, muscle_id):
    P.connect()

    try:
        muscle_dict = {}
        for muscle in P.Muscle(muscle_id).load():
            '''
                'neurons': list(muscle.neurons.get()),
                'receptors': list(muscle.receptors.get()),
            '''
            muscle_dict[str(muscle)] = {'name': str(muscle),
                                        'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/muscle.html',
                              {'muscle': muscle_dict[muscle_id]})


def Channels(request):
    P.connect()

    try:
        CHANNEL_DICT = {}
        for channel in P.Channel().load():
            CHANNEL_DICT[str(channel)] = {'name': str(channel),
                                          'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/channels.html',
                              {'channels': CHANNEL_DICT})


def Channel(request, channel_id):
    P.connect()

    try:
        channel_dict = {}
        for channel in P.Channel().load():
            channel_dict[str(channel)] = {'name': str(channel),
                                          'completeness': '#2B7558'}
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/channel.html',
                              {'channel': channel_dict[channel_id]})


def Evidences(request):
    P.connect()

    try:
        EVIDENCE_DICT = {}
        count = 0
        for evidence in P.Evidence().load():
            EVIDENCE_DICT[str(count)] = {
                'index': count,
                'doi': list(evidence.doi.get()),
                'pmid': list(evidence.pmid.get()),
                'wormbaseid': list(evidence.wbid.get()),
                'author': list(evidence.author.get()),
                'title': list(evidence.title.get()),
                'year': list(evidence.year.get()),
                'uri': list(evidence.uri.get()),
                'completeness': '#2B7558'}

            count += 1
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/evidences.html',
                              {'evidences': EVIDENCE_DICT})


def Evidence(request, evidence_id):
    P.connect()

    try:
        EVIDENCE_DICT = {}
        count = 0
        for evidence in P.Evidence().load():
            EVIDENCE_DICT[str(count)] = {
                'doi': list(evidence.doi.get()),
                'pmid': list(evidence.pmid.get()),
                'wormbaseid': list(evidence.wbid.get()),
                'author': list(evidence.author.get()),
                'title': list(evidence.title.get()),
                'year': list(evidence.year.get()),
                'uri': list(evidence.uri.get()),
                'completeness': '#2B7558'}

            count += 1
    finally:
        P.disconnect()

    return render_to_response('pyopenworm/evidence.html',
                              {'evidence': EVIDENCE_DICT[evidence_id]})


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

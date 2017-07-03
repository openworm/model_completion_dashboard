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

def Landing(request):
    return render(request, 'pyopenworm/landing.html')

def index(request):
    return render(request, 'pyopenworm/landing.html')

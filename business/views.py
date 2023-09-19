import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView
from django_htmx.http import HttpResponseClientRedirect

from .forms import MagasinModalForm
# Create your views here.
from .models import Store

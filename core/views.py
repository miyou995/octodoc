



from django.shortcuts import get_object_or_404, redirect, render
import weasyprint
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import (CreateView, DetailView, TemplateView,
                                  UpdateView, View)



# def index_view(request):
#     return redirect('admin:index')

def index_view(request):
    return render(request,'index.html')

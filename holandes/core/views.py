# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.views.generic import CreateView, ListView
#from django.core.urlresolvers import reverse_lazy
#from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

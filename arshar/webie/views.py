from django.shortcuts import render
from webie.models import *
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
# Create your views here.
class homepageview(ListView):
    model = Webie
    template_name = 'webie/index.html'
    
class contactpageview(CreateView):
    model = contactform
    template_name = 'webie/contact.html'
    fields= '__all__'
    
class inner_pageview(ListView):
    model = Webie
    template_name = 'webie/inner_page.html'
    
class portfolio_detailspageview(ListView):
    model = Webie
    template_name = 'webie/portfolio_details.html'
    
class servicepageview(ListView):
    model = Webie
    template_name = 'webie/services.html'
    
class aboutpageview(ListView):
    model = Webie
    template_name = 'webie/about.html'

    
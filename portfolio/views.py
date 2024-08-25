from django.shortcuts import render 

from django.views import generic
from .models import Portfolio

# Create your views here.
class Portfolio(generic.ListView):
    model = Portfolio
    context_object_name = "port"
    template_name = 'portfolio/portfolio_list.html'
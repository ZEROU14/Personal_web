from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
# Create your views here.
# def page_view(reqest,):
#     return  HttpResponse('hello')

class HomePageView(TemplateView):
    template_name = 'home.html'
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Client, TitleOne, WhatIdo
from django.views import generic
from blogs.models import Blogs
from django.urls import reverse_lazy

# Create your views here.
# def page_view(reqest,):
#     return  HttpResponse('hello')

# class HomePageView(generic.ListView):
#     template_name = 'home.html'
#     model = Client 
#     context_object_name = 'clients'

def homepage(request):
    Clients = Client.objects.all()
    Blog = Blogs.objects.all()
    Title = TitleOne.objects.get(pk=3)
    WhatIdos = WhatIdo.objects.all()


    return render(request , 'home.html',{'client': Clients,
                                         'blog': Blog,
                                         'title': Title,
                                         'whatido': WhatIdos,
                                         })


class ContactPageView(generic.CreateView):
    model = Question
    fields = ["Full_name", "Email", "Subject", "Message"]
    context_object_name = 'forms'
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('contact')
    
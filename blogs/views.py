from django.shortcuts import render
from django.views import generic

from .models import Blogs


# Create your views here.
class BlogsView(generic.ListView):
    queryset = Blogs.objects.filter(active=True).order_by('-datetime_created')
    context_object_name = 'blogs'
    template_name = 'blogs/blogs_list.html'
    

class BlogDetailView(generic.DetailView):
    model = Blogs
    context_object_name = 'blogs'
    template_name  = 'blogs/blog_detail.html'
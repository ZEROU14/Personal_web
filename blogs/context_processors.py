from .models import Blogs

def blogs(request):
    blog = Blogs.objects.all()
    return {'blogs':blog}
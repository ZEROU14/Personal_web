from .models import Blogs

def blogs(request):
    # blogg = Blogs.objects.all()
    return {'blog':Blogs.objects.all()}
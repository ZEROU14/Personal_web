from django.shortcuts import render

from .models import Experience , Certificates, Knowledge

# Create your views here.
def resume_view(request):
    Experiences = Experience.objects.all()
    Certificatess = Certificates.objects.all()
    Knowledges = Knowledge.objects.all()
    return render(request,'resume/resume.html',{'experiences':Experiences,
                                                'certificatess':Certificatess,
                                                'knowledges':Knowledges,}) 

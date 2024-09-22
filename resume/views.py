from django.shortcuts import render

from .models import Experience , Certificates, Knowledge,Design ,Coding

# Create your views here.
def resume_view(request):
    Experiences = Experience.objects.all()
    Certificatess = Certificates.objects.all()
    Knowledges = Knowledge.objects.all()
    Designs = Design.objects.all()
    Codings = Coding.objects.all()
    return render(request,'resume/resume.html',{'experiences':Experiences,
                                                'certificatess':Certificatess,
                                                'knowledges':Knowledges,
                                                'designs':Designs,
                                                'codings':Codings}) 

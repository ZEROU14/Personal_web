from django.shortcuts import render

from .models import Experience , Certificates, Knowledge,Design ,Coding , Education

# Create your views here.
def resume_view(request):
    Experiences = Experience.objects.all()
    Certificatess = Certificates.objects.all()
    Knowledges = Knowledge.objects.all()
    Designs = Design.objects.all()
    Codings = Coding.objects.all()
    Educations = Education.objects.get(pk=1)

    return render(request,'resume/resume.html',{'experiences':Experiences,
                                                'certificatess':Certificatess,
                                                'knowledges':Knowledges,
                                                'designs':Designs,
                                                'codings':Codings,
                                                'educations':Educations,
                                                }) 

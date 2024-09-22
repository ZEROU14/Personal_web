from django.urls import path
from .views import ContactPageView,homepage

urlpatterns = [
    path('', homepage , name= 'home'),
    path('contact/',ContactPageView.as_view(), name= 'contact'),
   
]

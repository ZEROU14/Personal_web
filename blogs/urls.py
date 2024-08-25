from django.urls import path
from .views import BlogsView ,BlogDetailView


urlpatterns = [
    path('', BlogsView.as_view(), name= 'blogs_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_info'),
]

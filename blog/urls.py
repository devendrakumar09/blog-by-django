from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('details', views.blogDetails, name='details'),
]

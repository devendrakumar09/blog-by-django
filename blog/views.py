from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog,Category
# INDEX PAGE
def index(request):
    categories = Category.objects.all()
    # template = loader.get_template('index.html')
    return render(request,'index.html',{'categories':categories})


# ABOUT PAGE
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


# BLOG PAGE
def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())


# CATEGORIES PAGE
def category(request):
    template = loader.get_template('category.html')
    return HttpResponse(template.render())


# CONTACT PAGE
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


# SEARCH PAGE
def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())


# BLOG DETAILS PAGE
def blogDetails(request):
    template = loader.get_template('single.html')
    return HttpResponse(template.render())


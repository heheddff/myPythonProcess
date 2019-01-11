from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    #return render(request,'blog/index.html',{'hello':'Hello world,I will come'})
    #artile = models.Article.objects.get(pk=1) #pk=primary_key
    artiles = models.Article.objects.all()  # pk=primary_key
    return render(request,'blog/index.html',{'artiles':artiles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/page.html',{'article':article})

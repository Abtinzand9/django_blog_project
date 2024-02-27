from django.shortcuts import render
from .models import Article

def home(request):
    context = {
        'articles' : Article.objects.all(),
        "publishs" : Article.publish.all()
    }
    return render(request , 'index.html' , context=context)

def blog_detail(request , pk):
    context ={
        "article":Article.objects.get(id = pk)
    }
    return render(request , 'posts/post_detail.html',context)
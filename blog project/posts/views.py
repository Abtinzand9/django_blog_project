from django.shortcuts import render
from .models import Article

def blog_list(request):
    context = {
        'articles' : Article.objects.all(),
        "publishs" : Article.publish.all()
    }
    return render(request , 'posts/post_list.html' , context=context)
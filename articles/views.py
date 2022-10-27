from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def articles(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'articles/articles.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request,):
    posts = Post.objects
    return render(request, 'blog/home.html', {'posts':posts,} )

def about(request):
    return render(request, 'blog/about.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post_detail': post_detail,})

def project(request):
    posts = Post.objects
    return render(request, 'blog/project.html', {'posts':posts})

def contact(request):
    return render(request, 'blog/contact.html')


def extra(request):
    return render(request, 'blog/extra.html')
from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts':post})


def post(request, id:str):
    posts = Post.objects.get(id=id)
    return render(request, 'post.html', {'post':posts})
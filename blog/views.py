from django.shortcuts import render
from .models import Post

# Create your views here.
def home(requests):
    p = Post.objects.all()
    context_dict = {'post' : p}
    return render(requests, 'home.html', context_dict)

from django.shortcuts import render
from django.utils import timezone
from django.template import loader

from .models import Post

# CMS - Views

# Lista os posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cms/post_list.html', {})


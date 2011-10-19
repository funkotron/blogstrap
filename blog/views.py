from django.shortcuts import render_to_response
from django.conf import settings
from django.template.context import RequestContext
from blog.models import Post, Tag, Social
#import os, markdown

def get_context(request,attrs=None):
    #raw_pages = os.listdir(os.path.abspath("templates/pages"))
    pages = Post.objects.filter(page=True)
    tags = Tag.objects.all()
    socials = Social.objects.all()
    a = {
        'site': settings.SITE_META,
        'pages': pages,
        'tags': tags,
        'socials': socials,
    }
    if attrs:
        a.update(attrs)
    return  RequestContext(request,a)

def index(request):
    posts = Post.objects.filter(page=False).order_by('-datetime')[:5]
    c = get_context(request,{
        'posts': posts,
        'active_page': 'home',
    })
    return render_to_response('index.html', c)

def post(request, post_slug=None):
    post = Post.objects.get(slug=post_slug)
    c = get_context(request,{
        'post': post,
        'active_page': post.slug
    })
    return render_to_response('post.html', c)




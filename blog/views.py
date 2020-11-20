from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Post
import markdown
from django.shortcuts import get_object_or_404, render
from .models import Post, Category, Tag
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        #'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    #post.toc = md.toc

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def author(request, pk):
    #post = get_object_or_404(Post, pk = pk) #不知道为什么，这边Post为空
    #post_list = Post.objects.filter(author=author).order_by('-created_time')
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post': post_list})
    return HttpResponse('<h1>hello world</h1>')


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})
    #return render(request, 'blog/index.html', context={'hello':'Hello World!'})



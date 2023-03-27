from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post, Tag
from typing import List


def posts_list(request: HttpRequest) -> HttpResponse:
    posts: List[Post] = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post: Post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request: HttpRequest) -> HttpResponse:
    tags: List[Tag] = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_detail(request: HttpRequest, slug: str) -> HttpResponse:
    tag: Tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})

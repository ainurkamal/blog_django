from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag
from typing import List


def posts_list(request: HttpRequest) -> HttpResponse:
    posts: List[Post] = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        post: Post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request: HttpRequest) -> HttpResponse:
    tags: List[Tag] = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        tag: Tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})


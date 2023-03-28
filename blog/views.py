from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm

from typing import List
from typing import Type, Any


def posts_list(request: HttpRequest) -> HttpResponse:
    posts: List[Post] = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model: Type[Any] = Post
    template: str = 'blog/post_detail.html'


def tags_list(request: HttpRequest) -> HttpResponse:
    tags: List[Tag] = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model: Type[Any] = Tag
    template: str = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self: 'TagCreate', request: HttpRequest) -> HttpResponse:
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

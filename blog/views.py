from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm, PostForm

from typing import List
from typing import Type, Any


def posts_list(request: HttpRequest) -> HttpResponse:
    posts: List[Post] = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model: Type[Any] = Post
    template: str = 'blog/post_detail.html'


class PostCreate(View):
    def get(self: 'PostCreate', request: HttpRequest) -> HttpResponse:
        form: PostForm = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form': form})

    def post(self: 'PostCreate', request: HttpRequest) -> HttpResponse:
        bound_form: PostForm = PostForm(request.POST)
        if bound_form.is_valid():
            new_post: Post = bound_form.save()
            return render(request, 'blog/post_create_form.html', context={'form': bound_form})


def tags_list(request: HttpRequest) -> HttpResponse:
    tags: List[Tag] = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model: Type[Any] = Tag
    template: str = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self: 'TagCreate', request: HttpRequest) -> HttpResponse:
        form: TagForm = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self: 'TagCreate', request: HttpRequest) -> HttpResponse:
        bound_form: TagForm = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag: Tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

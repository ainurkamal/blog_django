from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from typing import List, Type, Any


def posts_list(request: HttpRequest) -> HttpResponse:
    """
    Returns a response containing a list of all the posts.
    A response containing a list of all the posts.
    """
    posts: List[Post] = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    """
    Displays the details of a Post object.
    """
    model: Type[Any] = Post
    template: str = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin , View):
    """
    Controller for creating a new blog post.
    """
    form_model: Type[Any] = PostForm
    template: str = 'blog/post_create_form.html'
    raise_exception: bool = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """
    Controller for updating a blog post.
    """
    model: Type[Any] = Post
    form_model: Type[Any] = PostForm
    template: str = 'blog/post_update_form.html'
    raise_exception: bool = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """
    Controller for deleting a blog post.
    """
    model: Type[Any] = Post
    template: str = 'blog/post_delete_form.html'
    redirect_url: str = 'posts_list_url'
    raise_exception: bool = True


def tags_list(request: HttpRequest) -> HttpResponse:
    """
    Returns a response containing a list of all the tags.
    A response containing a list of all the tags.
    """
    tags: List[Tag] = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    """
    Displays the details of a Tag object.
    """
    model: Type[Any] = Tag
    template: str = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """
    Controller for creating a new tag.
    """
    form_model: Type[Any] = TagForm
    template: str = 'blog/tag_create.html'
    raise_exception: bool = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """
    Controller for updating a tag.
    """
    model: Type[Any] = Tag
    form_model: Type[Any] = TagForm
    template: str = 'blog/tag_update_form.html'
    raise_exception: bool = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """
    Controller for deleting a tag.
    """
    model: Type[Any] = Tag
    template: str = 'blog/tag_delete_form.html'
    redirect_url: str = 'tags_list_url'
    raise_exception: bool = True
    

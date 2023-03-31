from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
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


class PostCreate(ObjectCreateMixin , View):
    """
    Controller for creating a new blog post.
    """
    form_model: Type[Any] = PostForm
    template: str = 'blog/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    """
    Controller for updating a blog post.
    """
    model: Type[Any] = Post
    form_model: Type[Any] = PostForm
    template: str = 'blog/post_update_form.html'


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


class TagCreate(ObjectCreateMixin, View):
    """
    Controller for creating a new tag.
    """
    form_model: Type[Any] = TagForm
    template: str = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    """
    Controller for updating a tag.
    """
    model: Type[Any] = Tag
    form_model: Type[Any] = TagForm
    template: str = 'blog/tag_update_form.html'


class TagDelete(View):
    """
    Controller for deleting a tag.
    """
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        """
        Renders the form to delete the object.
        A response containing the mapping of an object using a template.
        """
        tag: Any = Tag.objects.get(slug__iexact=slug)
        return render(
            request, 'blog/tag_delete_form.html',
            context={'tag': tag}
        )
    
    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        """
        Handles the form submission and deletes the object.
        A response containing the mapping of an object using a template.
        """
        tag: Any = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))
    

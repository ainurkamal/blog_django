from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from .models import Post, Tag
from .utils import ObjectDetailMixin
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


class PostCreate(View):
    """
    Creates a new Post object.
    A response containing a form for creating a new Post object.
    """

    def get(self: 'PostCreate', request: HttpRequest) -> HttpResponse:
        """Displays a form for creating a new Post object."""
        form: PostForm = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form': form})

    def post(self: 'PostCreate', request: HttpRequest) -> HttpResponse:
        """Creates a new Post object from the form data."""
        bound_form: PostForm = PostForm(request.POST)
        if bound_form.is_valid():
            new_post: Post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_create_form.html', context={'form': bound_form})


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


class TagCreate(View):
    """
    Creates a new Tag object.
    A response containing a form for creating a new Tag object.
    """

    def get(self: 'TagCreate', request: HttpRequest) -> HttpResponse:
        """Returns a HttpResponse containing a form for creating a new Tag object."""
        form: TagForm = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self: 'TagCreate', request: HttpRequest) -> HttpResponse:
        """Creates a new Tag object from the form data."""
        bound_form: TagForm = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag: Tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

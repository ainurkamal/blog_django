from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.paginator import Paginator, Page, EmptyPage

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from typing import List, Type, Any, Union


def posts_list(request: HttpRequest) -> HttpResponse:
    """
    Renders a paginated list of all the posts in the database.
    The posts are ordered by the date created, newest first.

    Returns HTTP response object, containing the rendered template.
    """
    search_query: str = request.GET.get('search', '')

    if search_query:
        posts: List[Post] = Post.objects.filter(
            Q(title__icontains=search_query)|
            Q(body__icontains=search_query)
        )
    else:
        posts: List[Post] = Post.objects.all()

    paginator: Paginator = Paginator(posts, 3)

    page_number: int = request.GET.get('page', 1)
    page: Union[Page, EmptyPage] = paginator.get_page(page_number)

    is_paginated: bool = page.has_other_pages()

    if page.has_previous():
        prev_url: str = f'?page={page.previous_page_number()}'
    else:
        prev_url: str = ''

    if page.has_next():
        next_url: str = f'?page={page.next_page_number()}'
    else:
        next_url: str = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'blog/index.html', context=context)


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

    

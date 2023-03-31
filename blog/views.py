from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
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


class TagUpdate(View):
    """
    Controller for updating a tag.
    """
    def get(self: 'TagUpdate', request: HttpRequest, slug: str) -> HttpResponse:
        tag: Tag = Tag.objects.get(slug__iexact=slug)
        bound_form: TagForm = TagForm(instance=tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    
    def post(self: 'TagUpdate', request: HttpRequest, slug: str) -> HttpResponse:
        """
        Updates a tag.
        """
        tag: Tag = Tag.objects.get(slug__iexact=slug)
        bound_form: TagForm = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag: Tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

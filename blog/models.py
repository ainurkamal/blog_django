from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile
from typing import Type, Any
from time import time


def generate_slug(title: str) -> str:
    """
    Generates a unique slug from the title.
    """
    new_slug: str = slugify(title, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post, limited to 150 characters.
        slug (str): The URL-friendly slug for the post, derived from the title.
        body (str): The body of the post, which can include HTML.
        tags (Type['Tag']): The tags associated with the post.
        date_pub (DateTimeField): The date and time the post was published.
    """
    title: str = models.CharField(max_length=150, db_index=True)
    slug: str = models.SlugField(max_length=150, blank=True, unique=True)
    body: str = models.TextField(blank=True, db_index=True)
    tags: Type['Tag'] = models.ManyToManyField(
        'Tag', blank=True, related_name='posts')
    image: InMemoryUploadedFile = models.ImageField(upload_to='images', blank=True, null=True)
    date_pub: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self: 'Post') -> str:
        """
        Return the URL to access a detail view for this post.
        """
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self: 'Post') -> str:
        """
        Return the URL to access a form to update this post.
        """
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self: 'Post') -> str:
        """
        Return the URL to access a form to delete this post.
        """
        return reverse('post_delete_url', kwargs={'slug': self.slug})
    
    def get_image_url(self):
        """
        Returns the URL of the post's image, or a default image if no image is attached.
        """
        if self.image:
            return self.image.url
        else:
            return '/static/images/default.jpg'

    def save(self: 'Post', *args: Any, **kwargs: Any) -> None:
        """
        Save this post to the database, generating a slug if one is not provided.
        """
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self: 'Post') -> str:
        """
        Return a string representation of this post.
        """
        return self.title
    
    class Meta:
        ordering: list = ['-date_pub']


class Tag(models.Model):
    """
    A model representing a tag.

    Attributes:
        title (str): The title of the tag, limited to 50 characters.
        slug (str): The URL-friendly slug for the tag, derived from the title.
    """
    title: str = models.CharField(max_length=50)
    slug: str = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self: 'Tag') -> str:
        """
        Return the URL to access a detail view for this tag.
        """
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self: 'Tag') -> str:
        """
        Return the URL to access a form to update this tag.
        """
        return reverse('tag_update_url', kwargs={'slug': self.slug})
    
    def get_delete_url(self: 'Tag') -> str:
        """
        Return the URL to access a form to delete this tag.
        """
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self: 'Tag') -> str:
        """
        Return a string representation of this tag.
        """
        return f'{self.title}'
    
    class Meta:
        ordering: list = ['title']


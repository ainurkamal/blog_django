from django.db import models
from django.shortcuts import reverse
from typing import Type


class Post(models.Model):
    title: str = models.CharField(max_length=150, db_index=True)
    slug: str = models.SlugField(max_length=150, unique=True)
    body: str = models.TextField(blank=True, db_index=True)
    tags: Type['Tag'] = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self: 'Post') -> str:
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self: 'Post') -> str:
        return self.title


class Tag(models.Model):
    title: str = models.CharField(max_length=50)
    slug: str = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self: 'Tag') -> str:
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self: 'Tag') -> str:
        return f'{self.title}'

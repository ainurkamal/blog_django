from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError
from typing import List


class PostForm(forms.ModelForm):
    """
    A form for creating or updating a Post object.
    """
    class Meta:
        model: 'Post' = Post
        fields: List[str] = ['title', 'slug', 'body', 'tags']

        widgets: dict = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input slug'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input text'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        def clean_slug(self: 'PostForm') -> str:
            """
            Validates the 'slug' field to ensure that it is not the same as 'create'.
            Raises ValidationError if the 'slug' field is the same as 'create'.
            """
            new_slug: str = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug may not be "create"')
            return new_slug


class TagForm(forms.ModelForm):
    """
    A form for creating or updating a Tag object.
    """
    class Meta:
        model: 'Tag' = Tag
        fields: List[str] = ['title', 'slug']

        widgets: dict = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input slug'})
        }

    def clean_slug(self: 'TagForm') -> str:
        """
        Validates the 'slug' field to ensure that it is unique and not the same as 'create'.
        Raises ValidationError if the 'slug' field is not unique or is the same as 'create'.
        """
        new_slug: str = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise forms.ValidationError('Slug may not be "create"')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise forms.ValidationError(
                f'Slug must be unique. "{new_slug}" slug already exists')

        return new_slug

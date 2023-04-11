from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError
from typing import List


class PostForm(forms.ModelForm):
    """
    A form for creating or updating a Post object.
    """
    image = forms.ImageField(required=False)

    class Meta:
        model: 'Post' = Post
        fields: List[str] = ['title', 'slug', 'body', 'tags', 'image']

        widgets: dict = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок поста'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите уникальный адрес поста'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст поста'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

        def clean_slug(self: 'PostForm') -> str:
            """
            Validates the 'slug' field to ensure that it is not the same as 'create'.
            Raises ValidationError if the 'slug' field is the same as 'create'.
            """
            new_slug: str = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError(f'Адрес тега должен быть уникальным. "{new_slug}" уже используется.')
            return new_slug


class TagForm(forms.ModelForm):
    """
    A form for creating or updating a Tag object.
    """
    class Meta:
        model: 'Tag' = Tag
        fields: List[str] = ['title', 'slug']

        widgets: dict = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите загловок тега'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите уникальный адрес тега'})
        }

    def clean_slug(self: 'TagForm') -> str:
        """
        Validates the 'slug' field to ensure that it is unique and not the same as 'create'.
        Raises ValidationError if the 'slug' field is not unique or is the same as 'create'.
        """
        new_slug: str = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise forms.ValidationError('Уникальный адрес тега не может быть "create"')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise forms.ValidationError(
                f'Адрес тега должен быть уникальным. "{new_slug}" уже используется.')

        return new_slug

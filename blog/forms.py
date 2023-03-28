from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title: str = forms.CharField(max_length=50)
    slug: str = forms.SlugField(max_length=50)

    def clean_slug(self: 'TagForm') -> str:
        new_slug: str = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise forms.ValidationError('Slug may not be "Create"')
        return new_slug

    def save(self: 'TagForm') -> None:
        new_tag: 'Tag' = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug']
        )
        return new_tag

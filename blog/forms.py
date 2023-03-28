from django import forms
from .models import Tag
from django.core.exceptions import ValidationError
from typing import List


class TagForm(forms.ModelForm):
    class Meta:
        model: 'Tag' = Tag
        fields: List[str] = ['title', 'slug']

        widgets: dict = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self: 'TagForm') -> str:
        new_slug: str = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise forms.ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise forms.ValidationError(f'Slug must be unique. "{new_slug}" slug already exists')
        return new_slug

from django import forms
from .models import Tag


class TagForm(forms.Form):
    title: str = forms.CharField(max_length=50)
    slug: str = forms.SlugField(max_length=50)

    def save(self: 'TagForm') -> None:
        new_tag: 'Tag' = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug']
        )
        return new_tag

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from typing import Type, Any

from .models import *


class ObjectDetailMixin:
    """
    A mixin that provides common functionality for views,
    which display the details of an object.
    """
    model: Type[Any] = None
    template: str = None

    def get(self, request: Any, slug: str) -> Any:
        """
        Gets an object and renders it using a template.
        A response containing the mapping of an object using a template.
        """
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

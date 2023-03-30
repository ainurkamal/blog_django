from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from typing import Type, Any
from django.http import HttpRequest, HttpResponse

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
    

class ObjectCreateMixin:
    """
    Mixin class for creating a new object using a form. 
    It provides a `get` method that renders the form to create the new object, 
    and a `post` method that handles the form submission and creation of the new object.
    """
    form_model: Type[Any] = None
    template: str = None

    def get(self, request: HttpRequest) -> HttpResponse:
        """Renders the form to create the new object."""
        form: Any = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        """Handles the form submission and creation of the new object."""
        bound_form: Any = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

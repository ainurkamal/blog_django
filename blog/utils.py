from django.shortcuts import render
from django.shortcuts import get_object_or_404
from typing import Type, Any

from .models import *


class ObjectDetailMixin:
    """
     A mixin that provides common functionality for views,
     which display the details of an object.

     Attributes:
     ---------
     model : Type[Any]
         The model that will be used to get the object.
     template : str
         The path to the template that will be used to render the object.
     """
    model: Type[Any] = None
    template: str = None

    def get(self, request: Any, slug: str) -> Any:
        """
         Gets an object and renders it using a template.

         Options:
         ----------
         request : HttpRequest
             The request object that will be used to render the template.
         slug : str
             The slug value for the object.

         Returns:
         -----------
         HttpResponse
             A response containing the mapping of an object using a template.
         """
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

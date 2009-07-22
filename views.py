from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from thespians.models import *


def person_detail(request, slug, **kwargs):
    return list_detail.object_detail(
        request,
        queryset = Person.objects.all(),
        slug = slug,
        **kwargs
    )
person_detail.__doc__ = list_detail.object_detail.__doc__


def person_list(request, paginate_by=20, **kwargs):
    return list_detail.object_list(
        request,
        queryset = Person.objects.all(),
        paginate_by = paginate_by,
        **kwargs
    )
person_list.__doc__ = list_detail.object_list.__doc__



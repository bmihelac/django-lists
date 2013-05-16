from django import template
from django.contrib.contenttypes.models import ContentType

from lists.forms import ItemForm
from lists.util import (
        get_folder_from_request,
        get_folders_from_request,
        )

register = template.Library()


@register.assignment_tag
def lists_add_form(obj, folder_name=""):
    """
    Assigns form to add object ``obj`` to folder ``folder_name``.
    """
    ct = ContentType.objects.get_for_model(obj)
    data = {
            'folder_name': folder_name,
            'content_type': ct.pk,
            'object_id': obj.pk,
            }
    form = ItemForm(initial=data)
    return form


@register.assignment_tag
def lists_get_folders(request):
    """
    Returns all folders from request.
    """
    return get_folders_from_request(request)


@register.assignment_tag
def lists_get_folder(request, folder_name):
    """
    Returns folder named ``folder_name``.
    """
    folder = get_folder_from_request(request, folder_name)
    return folder


@register.assignment_tag
def lists_get_item(folder, obj):
    """
    Returns folder item for obj.
    """
    return folder.get_item(obj)


@register.filter
def content_type_id(obj):
    ct = ContentType.objects.get_for_model(obj)
    return ct.pk


@register.filter
def list_has_object(folder, obj):
    return bool(folder.get_item(obj))

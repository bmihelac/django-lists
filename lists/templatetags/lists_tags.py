from django import template
from django.contrib.contenttypes.models import ContentType

from lists.forms import ItemForm
from lists.util import get_folders_from_request

register = template.Library()


@register.inclusion_tag("lists/_item_add_form.html")
def lists_add_form(obj, folder_name=""):
    """
    Renders forms to add object ``obj`` to folder ``folder_name``.

    Template:

    * lists/_item_add_form.html
    """
    ct = ContentType.objects.get_for_model(obj)
    data = {
            'folder_name': folder_name,
            'content_type': ct.pk,
            'object_id': obj.pk,
            }
    form = ItemForm(initial=data)
    return {
            'form': form,
            }


@register.assignment_tag
def lists_get_folders(request):
    """
    Returns all folders from request.
    """
    return get_folders_from_request(request)

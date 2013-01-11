from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError
from django.views.generic import (
        FormView,
        DeleteView,
        DetailView,
        ListView,
        )

from .forms import ItemForm
from .models import Item, Folder
from .util import add_item_to_folder, get_folder_from_request


class FolderListView(ListView):
    model = Folder


class FolderDetailView(DetailView):
    model = Folder


class ItemCreateView(FormView):
    form_class = ItemForm
    template_name = "lists/item_form.html"
    redirect_field_name = "next"

    def form_valid(self, form):
        ct = get_object_or_404(ContentType,
                pk=form.cleaned_data['content_type'])
        obj = get_object_or_404(ct.model_class(),
                pk=form.cleaned_data['object_id'])
        folder_name = form.cleaned_data['folder_name']
        try:
            self.object = add_item_to_folder(self.request,
                    folder_name, obj)
        except IntegrityError:
            # object is already added, do nothing
            folder = get_folder_from_request(self.request, folder_name)
            self.object = folder.get_item(obj)
        if self.request.is_ajax():
            return HttpResponse('Ok<br>')
        else:
            return super(ItemCreateView, self).form_valid(form)

    def get_success_url(self):
        next = self.request.REQUEST.get(self.redirect_field_name)
        return next or self.object.folder.get_absolute_url()


class ItemDeleteView(DeleteView):
    model = Item
    redirect_field_name = "next"

    def get_success_url(self):
        next = self.request.REQUEST.get(self.redirect_field_name)
        return next or self.object.folder.get_absolute_url()

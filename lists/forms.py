from django import forms


class ItemForm(forms.Form):
    folder_name = forms.CharField(required=False,
            widget=forms.widgets.HiddenInput)
    content_type = forms.CharField(widget=forms.widgets.HiddenInput)
    object_id = forms.CharField(widget=forms.widgets.HiddenInput)

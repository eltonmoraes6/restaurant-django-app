from django import forms

from .models import Items, PageSection


class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        fields = ["page", "section", "title", "content", "image"]


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["Item_name", "Category", "Price", "description", "Image"]

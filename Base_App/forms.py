from django import forms

from .models import Category


from .models import Items, PageSection


class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        fields = ["page", "section", "title", "content", "image"]


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["Item_name", "Category", "Price", "description", "Image"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da categoria',
            }),
        }
        labels = {
            'name': 'Categoria',
        }
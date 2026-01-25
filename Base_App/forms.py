from django import forms

from .models import Category, Items, PageSection


class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        fields = ["page", "section", "title", "content", "image"]


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["Item_name", "Category", "Price", "description", "Image"]

        widgets = {
            "Item_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome do produto"
            }),
            "Category": forms.Select(attrs={
                "class": "form-select"
            }),
            "Price": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "Image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
                "onchange": "previewImage(this)"
            }),
        }

        labels = {
            "Item_name": "Nome do Produto",
            "Price": "Preço",
            "Image": "Imagem do Produto",
        }


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
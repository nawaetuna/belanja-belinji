from django.forms import ModelForm
from main.models import ProductEntry
from django import forms
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description", "quantity"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

from django import forms
from .models import GroceryItem


class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'e.g. eggs',
                    'required': True,
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Item name cannot be empty.')
        if len(name) > 200:
            raise forms.ValidationError('Item name is too long.')
        return name

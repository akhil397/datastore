from django import forms
from .models import CodeModels

class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeModels
        fields = ['title', 'code_lang', 'codes', 'description', 'type_code', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'code_lang': forms.Select(attrs={'class': 'form-control'}),  # Assuming this is a foreign key dropdown
            'codes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'type_code': forms.Select(attrs={'class': 'form-control'}),  # Assuming this is a foreign key dropdown
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

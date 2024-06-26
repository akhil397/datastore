from django import forms
from .models import CodeModels

class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeModels
        fields = ['title', 'code_lang', 'codes', 'description', 'type_code', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code_lang': forms.Select(attrs={'class': 'form-control'}),
            'codes': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type_code': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
from django import forms
from .models import SvgFile
from django.forms import ClearableFileInput

class SvgFileForm(forms.ModelForm):
    
    class Meta:
        model = SvgFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
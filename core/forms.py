from django import forms
from django.forms import ModelForm

from core.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['headline', 'content']
        widgets = {
            'headline': forms.TextInput(attrs={
                'id': 'headline', 
                'required': True, 
                'placeholder': 'Headline'
            }),
            'content': forms.Textarea(attrs={
                'id': 'content', 
                'required': True, 
                'placeholder': 'Content'
            }),
        }
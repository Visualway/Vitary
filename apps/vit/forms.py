from django import forms
from .models import Vit, Comment


class VitForm(forms.ModelForm):
    class Meta:
        model = Vit
        fields = ['body', 'image', 'video']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'What\'s on your mind?', 'id': 'body'}),
            'image': forms.FileInput(attrs={'class': 'file-input', 'style': '''width: 100%;''', 'id': 'image'}),
            'video': forms.FileInput(attrs={'class': 'file-input', 'style': '''width: 100%;''', 'id': 'video'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'textarea', 'id': 'body'}),
        }
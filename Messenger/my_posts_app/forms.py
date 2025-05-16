from django import forms
from .models import User_Post

class PostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields = [
            'title',
            'topic',
            'tags',
            'text',
            'links',
            'images',
            'views',
            'likes',
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Напишіть назву публікації",
                "class": "modal-testarea" 
            }),
            "topic": forms.TextInput(attrs={
                "placeholder": "Напишіть тему публікаціїї"
            })
            
        }
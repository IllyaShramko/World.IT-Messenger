from django import forms
from .models import Post



# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=150,
#         required=True,
#         widget= forms.TextInput(attrs={
#             "placeholder": "Напишіть назву публікації"
#         })
#     )
#     topic = forms.CharField(
#         max_length=150,
#         required=True,
#         widget= forms.TextInput(attrs={
#             "placeholder": "Напишіть тему публікації"
#         })
#     )
#     text = forms.CharField(
#         required=True,
#         widget= forms.Textarea()
#     )
#     links = forms.CharField(
#         required=True
#     )
#     images = forms.ImageField(
#         required=True
#     )

class PostForm(forms.ModelForm):
    topic = forms.CharField(
        max_length=150,
        required=True,
        label="Тема публікації",
        widget=forms.TextInput(attrs={
            "placeholder": "Напишіть тему публікації"
        })
    )
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]
        
        labels = {
            'title': "Назва публікації",
            'links': "Посилання",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Напишіть назву публікації"
            }),
            "content": forms.Textarea(attrs={
                "id": "text"
            }),
        }
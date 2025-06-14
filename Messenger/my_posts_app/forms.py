from django import forms
from .models import User_Post



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
    class Meta:
        model = User_Post
        fields = [
            'title',
            'topic',
            'text',
        ]
        
        labels = {
            'title': "Назва публікації",
            'topic': "Тема публікації",
            'links': "Посилання",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Напишіть назву публікації"
            }),
            "topic": forms.TextInput(attrs={
                "placeholder": "Напишіть тему публікаціїї"
            }),
            "text": forms.Textarea(attrs={
                "id": "text"
            }),
        }
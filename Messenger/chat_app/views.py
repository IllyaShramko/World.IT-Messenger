from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ChatsView(TemplateView):
    template_name = "chat_app/chats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "chats"
        return context
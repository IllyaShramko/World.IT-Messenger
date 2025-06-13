from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

class ChatsView(TemplateView):
    template_name = "chat_app/chats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "chats"
        context['contacts'] = self.request.user.friends.all()
        context['chat'] = True
        return context  
    
    def post(self, request: HttpRequest):
        button = request.POST.get('button')
        print(button)
        if button == "contactOpen":
            return render(
                request,
                "chat_app/chats.html",
                context = {
                    "messages": ...,
                    "groups": ...,
                }
            )
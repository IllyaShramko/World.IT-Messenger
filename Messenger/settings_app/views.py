from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SettingsView(TemplateView):
    template_name = "settings_app/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'settings'
        return context
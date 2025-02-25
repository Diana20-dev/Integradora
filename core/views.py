from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"¿Buscas o te están buscando?"})

class EmpleoPageView(TemplateView):
    template_name = "core/empleo.html"
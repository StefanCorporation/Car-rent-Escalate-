from typing import Any

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView



from .models import VehiclesForRent
from users.models import Users



class HomeView(ListView):
    model = VehiclesForRent
    template_name = 'index.html'
   
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['vehicles'] = VehiclesForRent.objects.filter(available=True)
        return context


def contact(request):
    return render(request, 'contact.html')









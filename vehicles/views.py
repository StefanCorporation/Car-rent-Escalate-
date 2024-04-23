from typing import Any

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import VehiclesForRent
from common.views import TitleMxin



class HomeView(TitleMxin, ListView):
    model = VehiclesForRent
    template_name = 'index.html'
    title = 'Escalate Rent Garage'
   
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['vehicles'] = VehiclesForRent.objects.filter(available=True)
        return context


class ContactView(TitleMxin, TemplateView):
    template_name = 'contact.html'
    title = 'Contact'











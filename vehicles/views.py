from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView


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





# def single_post(request, post_id):
#     post = get_object_or_404(VehiclesForRent, pk=post_id)

#     return render(request, 'single_post.html', {'single_post': post})




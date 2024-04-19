from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView


from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, RentDataForm
from .models import Users, RentData
from vehicles.models import VehiclesForRent


class UserProfileView(UpdateView):
    model = Users
    template_name = 'profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('users:login')
 

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
   


class RentView(CreateView):
    model = RentData
    template_name = 'single_post.html'
    form_class = RentDataForm
    success_url = reverse_lazy('vehicles:home')

    def get_context_data(self, **kwargs):
        context = super(RentView, self).get_context_data(**kwargs)
        post_id = self.kwargs.get('post_id')  
        context["single_post"] = get_object_or_404(VehiclesForRent, pk=post_id)
        return context

    def form_valid(self, form):
        post_id = self.kwargs.get('post_id')
        print(self.kwargs)

 
        form.instance.user_id = self.request.user.id
        form.instance.vehicle_for_rent_id = post_id
        return super().form_valid(form)



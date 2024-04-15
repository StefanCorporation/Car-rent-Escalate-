from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView


from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import Users




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
   
    
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView


from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, RentDataForm, PaymentForm
from .models import Users, RentData, PaymentData
from vehicles.models import VehiclesForRent
from common.views import TitleMxin

class UserProfileView(TitleMxin, UpdateView):
    model = Users
    template_name = 'profile.html'
    form_class = UserProfileForm
    title = 'Profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rent_data = RentData.objects.filter(user_id=self.request.user.id, paid=True).order_by('-created_at')
        context['rent_data'] = rent_data
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserRegistrationView(TitleMxin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('users:login')
    title = 'Registration'
 

class UserLoginView(TitleMxin, LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    title = 'Login'
   

class RentView(TitleMxin, CreateView):
    model = RentData
    template_name = 'single_post.html'
    form_class = RentDataForm
    title = 'Rent Form'
 

    def get_context_data(self, **kwargs):
        context = super(RentView, self).get_context_data(**kwargs)
        post_id = self.kwargs.get('post_id')  
        context["single_post"] = get_object_or_404(VehiclesForRent, pk=post_id)
        return context


    def form_valid(self, form):
        post_id = self.kwargs.get('post_id')
        form.instance.user_id = self.request.user.id
        form.instance.vehicle_for_rent_id = post_id
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('users:payment', kwargs={'user_id': self.request.user.id})


class PaymentView(TitleMxin, CreateView):
    model = PaymentData
    template_name = 'payment.html'
    form_class = PaymentForm
    success_url = reverse_lazy('users:profile')
    title = 'Payment'


    def form_valid(self, form):
        payment_data = form.save(commit=False)
        user_id = self.request.user.id
        rent_data = RentData.objects.filter(user_id=user_id).latest('created_at') 

    
        payment_data.rent_data = rent_data
        payment_data.save()

        rent_data.paid = True
        rent_data.save()

        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        last_rent_data = RentData.objects.filter(user_id=user_id).latest('created_at')
        context['rent_data'] = last_rent_data
        return context
    

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.request.user.id})
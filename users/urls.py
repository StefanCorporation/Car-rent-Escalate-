from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('rent/', views.RentView.as_view(), name='rent')
]

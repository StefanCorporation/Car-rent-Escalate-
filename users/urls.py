from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login')
]

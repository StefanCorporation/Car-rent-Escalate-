from django.urls import path

from . import views


app_name = 'vehicles'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
]


from django.urls import path

from . import views


app_name = 'vehicles'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]


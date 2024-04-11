from django.urls import path

from . import views


app_name = 'vehicles'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('single_post/<int:post_id>/', views.single_post, name='single_post')
]


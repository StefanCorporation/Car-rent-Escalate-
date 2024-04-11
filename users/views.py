from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')
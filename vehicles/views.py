from django.shortcuts import render, get_object_or_404

from .models import VehiclesForRent

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def single_post(request, post_id):
    post = get_object_or_404(VehiclesForRent, pk=post_id)
    print(post)

    return render(request, 'single_post.html', {'single_posts': post})
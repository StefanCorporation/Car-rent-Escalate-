from django.shortcuts import render, get_object_or_404

from .models import VehiclesForRent
from users.models import Users

def home(request):
    vehicles = VehiclesForRent.objects.filter(available=True)

    return render(request, 'index.html', {'vehicles': vehicles})


def contact(request):
    return render(request, 'contact.html')



def single_post(request, post_id):
    post = get_object_or_404(VehiclesForRent, pk=post_id)

    return render(request, 'single_post.html', {'single_post': post})
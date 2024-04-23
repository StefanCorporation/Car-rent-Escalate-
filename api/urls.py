from django.urls import path, include
from rest_framework import routers

from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'vehicles_for_rent_list', views.VehiclesForRentViewSet)
router.register(r'rent_data_list', views.RentDataViewSet)
router.register(r'users_list', views.UsersViewSet),
router.register(r'payment_list', views.PaymentDataViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)) #http://127.0.0.1:8000/escalate_rent/api/v1/vehicles_for_rent_list/
]
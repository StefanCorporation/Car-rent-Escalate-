from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from vehicles.models import VehiclesForRent
from users.models import RentData, Users, PaymentData

from api.serializers import VehiclesForRentSerializer, RentDataSerializer, UsersSerializers, PaymentSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class VehiclesForRentViewSet(ModelViewSet):
    queryset = VehiclesForRent.objects.all()
    serializer_class = VehiclesForRentSerializer


class RentDataViewSet(ModelViewSet):
    queryset = RentData.objects.all()
    serializer_class = RentDataSerializer


class PaymentDataViewSet(ModelViewSet):
    queryset = PaymentData.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment_data = serializer.save()
        print(self.request)
        rent_data_id = self.request.data.get('rent_data') 
        print(rent_data_id)

        rent_data = RentData.objects.get(pk=rent_data_id)
        
        rent_data.paid = True
        rent_data.save()

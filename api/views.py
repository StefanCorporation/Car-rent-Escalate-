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
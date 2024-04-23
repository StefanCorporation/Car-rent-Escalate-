from rest_framework import serializers

from vehicles.models import VehiclesForRent
from users.models import RentData, Users, PaymentData


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__' 



class VehiclesForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclesForRent
        fields = [
            'id', 'vehicle_image', 'logo', 'mark', 'model', 'color',
            'type', 'engine_val', 'fuel_type', 'gear_box', 'year',
            'title', 'about_vehicle', 'price', 'available', 'time_create',
            'time_update'
        ]


class RentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentData
        fields = [
            'id', 'user', 'vehicle_for_rent', 'username', 'email',
            'first_name', 'last_name', 'phone', 'pick_up_location',
            'leave_car_location', 'pick_up_time', 'return_time', 
            'pick_up_date', 'car_return_date', 'paid', 'created_at'
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentData
        fields = '__all__'
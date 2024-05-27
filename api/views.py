from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from vehicles.models import VehiclesForRent
from users.models import RentData, Users, PaymentData

from api.serializers import VehiclesForRentSerializer, RentDataSerializer, UsersSerializers, PaymentSerializer
from api.permissions import IsAdminOrReadOnly


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

    # Only admin has all permissions to (GET, POST, PUT, DELETE) or read ALL data!
    # Each authorized user only has access to personal information and can change it use (GET, POST, PUT, DELETE)
    def get_queryset(self):
        if self.request.user.is_staff:           
            return Users.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user_id = self.request.user.id
        return Users.objects.filter(pk=user_id)
    

class VehiclesForRentViewSet(ModelViewSet):
    queryset = VehiclesForRent.objects.all()
    serializer_class = VehiclesForRentSerializer
    permission_classes = [IsAdminOrReadOnly]



class RentDataViewSet(ModelViewSet):
    queryset = RentData.objects.all()
    serializer_class = RentDataSerializer

  



    # Only admin has all permissions to (GET, POST, PUT, DELETE) or read ALL data!
    # Each authorized user only has access to personal information and can change it use (GET, POST, PUT, DELETE)
    def get_queryset(self):
        if self.request.user.is_staff:           
            return RentData.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user_id = self.request.user.id
           
        return RentData.objects.filter(user=user_id)




class PaymentDataViewSet(ModelViewSet):
    queryset = PaymentData.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment_data = serializer.save()
        rent_data_id = self.request.data.get('rent_data') 

        rent_data = RentData.objects.get(pk=rent_data_id)
        
        rent_data.paid = True
        rent_data.save()


    # Only admin has all permissions to (GET, POST, PUT, DELETE) or read ALL data!
    # Each authorized user only has access to personal information and can change it use (GET, POST, PUT, DELETE)
    def get_queryset(self):
        if self.request.user.is_staff:           
            return PaymentData.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user_id = self.request.user.id
           
        return PaymentData.objects.filter(rent_data__user = user_id)

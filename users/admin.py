from django.contrib import admin

from .models import Users, RentData, PaymentData

admin.site.register(Users)
admin.site.register(RentData)
admin.site.register(PaymentData)


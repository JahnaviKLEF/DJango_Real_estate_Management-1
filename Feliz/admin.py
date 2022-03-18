from django.contrib import admin

# Register your models here.
from .models import Customer,Sell


admin.site.register(Customer)
admin.site.register(Sell)

from django.contrib import admin
from .models import People,Peoplelist
from .models import Product,Productlist


admin.site.register(People,Peoplelist)

admin.site.register(Product,Productlist)

# Register your models here.

from django.contrib import admin
from .models import ProductType, Prodcut, Review

# Register your models here.
admin.site.register(ProductType)
admin.site.register(Prodcut)
admin.site.register(Review)
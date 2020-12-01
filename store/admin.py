from django.contrib import admin
from .models import Product, Gender


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'gender']
    ordering = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Gender)

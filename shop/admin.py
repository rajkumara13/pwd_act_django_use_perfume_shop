from django.contrib import admin
from .models import Perfume, CartItem

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('perfume', 'quantity')

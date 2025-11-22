from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfumes/', views.perfume_list, name='perfume_list'),
    path('perfume/<int:id>/', views.perfume_detail, name='perfume_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
]

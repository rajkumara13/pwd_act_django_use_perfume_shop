# perfume_shop/urls.py (or your main urls file)

from django.contrib import admin
from django.urls import path
from shop import views
# REQUIRED IMPORTS FOR SERVING MEDIA IN DEVELOPMENT
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('perfumes/', views.perfume_list, name='perfume_list'),
    path('perfume/<int:id>/', views.perfume_detail, name='perfume_detail'),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
]

# ESSENTIAL BLOCK TO SERVE MEDIA FILES (IMAGES) IN DEVELOPMENT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
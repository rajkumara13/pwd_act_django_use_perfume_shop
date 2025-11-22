from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume, CartItem

def home(request):
    return render(request, 'home.html')

def perfume_list(request):
    perfumes = Perfume.objects.all()
    return render(request, 'perfumes.html', {'perfumes': perfumes})

def perfume_detail(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    return render(request, 'perfume_detail.html', {'perfume': perfume})

def add_to_cart(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    item, created = CartItem.objects.get_or_create(perfume=perfume)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_view')

def cart_view(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

def checkout(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    if request.method == 'POST':
        items.delete()
        return render(request, 'checkout_success.html')
    return render(request, 'checkout.html', {'total': total})

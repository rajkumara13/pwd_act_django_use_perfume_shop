# D:\clg project\Pwd_act_perfume_shop\shop\views.py

from django.shortcuts import render, get_object_or_404, redirect # Import redirect
from django.http import HttpResponse # Import HttpResponse if needed
from .models import Perfume, CartItem # Assuming you have a CartItem model

def home(request):
    """View for the root URL, renders the home.html template."""
    return render(request, 'home.html') 

def perfume_list(request):
    """View to display the list of all perfumes."""
    all_perfumes = Perfume.objects.all() 
    context = {
        'perfumes': all_perfumes  # Used in the {% for perfume in perfumes %} loop
    }
    return render(request, 'perfumes.html', context) 

def perfume_detail(request, id):
    """View to display details of a single perfume."""
    perfume = get_object_or_404(Perfume, id=id)
    return render(request, 'perfume_detail.html', {'perfume': perfume})

# --- FIX: Define the missing add_to_cart view ---
def add_to_cart(request, id):
    """Handles adding a specific perfume to the user's cart."""
    # This is a basic placeholder. You will add your actual cart logic here.
    
    # 1. Fetch the perfume
    perfume = get_object_or_404(Perfume, id=id)
    
    # 2. Add item to cart logic goes here (requires user and cart model logic)
    # Example logic (requires authentication/session):
    # if request.user.is_authenticated:
    #     cart_item, created = CartItem.objects.get_or_create(
    #         user=request.user,
    #         perfume=perfume,
    #         defaults={'quantity': 1}
    #     )
    #     if not created:
    #         cart_item.quantity += 1
    #         cart_item.save()
            
    # 3. Redirect to the cart page after adding the item
    return redirect('cart_view') 

# --- Define the other missing views (cart_view, checkout) ---
def cart_view(request):
    # Logic to retrieve and display the cart contents
    return render(request, 'cart.html')

def checkout(request):
    # Logic for the checkout process
    return render(request, 'checkout.html')
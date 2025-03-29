from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.contrib import messages
from django.http import JsonResponse

def cart_summary(request):
    cart=Cart(request)
    cart_products = cart.get_pords()
    totals=cart.total()
    quantities=cart.get_quants #for quantities
    return render(request, 'cart_summary.html', {'cart_products': cart_products,"quantities":quantities,"totals":totals})

def cart_add(request):
    cart = Cart(request)
    
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product,quantity=product_qty)
        
        # Print cart contents for debugging
        # print(request.session.get('session_key'))  
        
        cart_quantity = cart.__len__()
        messages.success(request, 'You  successfully added item to cart')
        return JsonResponse({'qty': cart_quantity})


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product=get_object_or_404(Product,id=product_id)
        cart.delete(product=product)
        response = JsonResponse({'product': product_id})
        messages.success(request, 'You  successfully remove the  product from cart')
        return response
    

    

def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            product = get_object_or_404(Product, id=product_id)  # Ensure the product object is retrieved
            cart.update(product=product, quantity=product_qty)  # Pass the product object to the update method
            response = JsonResponse({'qty': product_qty})
            messages.success(request, 'You  successfully update the quantity of the product')
            return response
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)


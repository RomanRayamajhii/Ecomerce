from django.shortcuts import render
from cart.cart import Cart
from payment.forms import Shippingform,PaymentForm
from payment.models import ShippingAddress
from payment.models import Order, OrderItem
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from store.models import Profile,Product
import datetime



def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(pk=pk)
        order_items = OrderItem.objects.filter(order=pk)
        
        if request.POST:
            status=request.POST['shipping_status']
            if status== 'true':
                order=Order.objects.filter(pk=pk)
                #update status
                now = datetime.datetime.now()
                order.update(shipped=True,date_shipped=now)
            else:
                order=Order.objects.filter(pk=pk)
                #update status
                
                order.update(shipped=False)
            messages.success(request, 'Order status updated successfully!')
            return redirect('index')        
                
                
            
        return render(request, 'orders.html', {'order': order, 'order_items': order_items})
    else:
        messages.success(request, 'Access Denied')
        return redirect('index')

def unshipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        if request.POST:
            num=request.POST['num']
            status=request.POST['shipping_status']
            
            order=Order.objects.filter(pk=num)
                #update status
            now = datetime.datetime.now()
            order.update(shipped=True,date_shipped=now)
          
            
            messages.success(request, 'Order status updated successfully!')
            return redirect('unshipped_dash')   
        return render(request, 'unshipped_dash.html', {'orders': orders})
    else:
        messages.success(request, 'Access Denied')
        return redirect('index')


def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        
        orders = Order.objects.filter(shipped=True)
        if request.POST:
            num=request.POST['num']
            status=request.POST['shipping_status']
            order=Order.objects.filter(id=num)
            
                #update status
            now = datetime.datetime.now()
            order.update(shipped=False)
          
            
            messages.success(request, 'Order status updated successfully!')
            return redirect('shipped_dash')  
        return render(request, 'shipped_dash.html', {'orders': orders})
    else:
        messages.success(request, 'Access Denied')
        return redirect('index')   



def payment_success(request):
    return render(request,'payment_success.html',{})
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_pords()
    totals = cart.total()
    quantities = cart.get_quants  # for quantities
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user=request.user)
        Shipping_form = Shippingform(request.POST or None, instance=shipping_user)
        if request.method == 'POST' and Shipping_form.is_valid():
            Shipping_form.save()  # Save the form, including the zipcode
            messages.success(request, 'Shipping information updated successfully!')
            return redirect('billing_info')
        return render(request, 'checkout.html', {
            'cart_products': cart_products,
            "quantities": quantities,
            "totals": totals,
            'Shipping_form': Shipping_form  # Changed to 'Shipping_form'
        })
    else:
        # as guest
        Shipping_form = Shippingform(request.POST or None)
        return render(request, 'checkout.html', {
            'cart_products': cart_products,
            "quantities": quantities,
            "totals": totals,
            'Shipping_form': Shipping_form  # Changed to 'Shipping_form'
        })
def billing_info(request):
    if request.POST:
        cart=Cart(request)
        cart_products = cart.get_pords()
        totals=cart.total()
        quantities=cart.get_quants #for quantities
        # create session for shipping info
        my_shipping=request.POST
        request.session['my_shipping']=my_shipping
        
        if request.user.is_authenticated:
            billing_form=PaymentForm(request.POST)
            return render(request, 'billing_info.html', {'cart_products': cart_products,"quantities":quantities,"totals":totals,'Shipping_info':request.POST,'billing_form':billing_form})
        else:
            billing_form=PaymentForm(request.POST)
            return render(request, 'billing_info.html', {'cart_products': cart_products,"quantities":quantities,"totals":totals,'Shipping_info':request.POST,'billing_form':billing_form})
            
            
        Shipping_form=request.POST
        return render(request, 'billing_info.html', {'cart_products': cart_products,"quantities":quantities,"totals":totals,'Shipping_form':Shipping_form,'billing_form':billing_form})
    else:
        messages.success(request, 'You need to login first')
        return redirect('index')
def process_order(request):
    if request.POST:
        
        cart=Cart(request)
        cart_products = cart.get_pords()
        totals=cart.total()
        quantities=cart.get_quants 
        payment_form=PaymentForm(request.POST or None)
        my_shipping=request.session.get('my_shipping')
        full_name=my_shipping['shippingfull_name']
        email=my_shipping['shipping_EmailAddress']
        phone_number=my_shipping['shipping_phonenumber']
        shipping_address=f"{my_shipping['shipping_country']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_district']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_zipCode']}\n{my_shipping['shipping_phonenumber']}\n"
        amount_paid=totals
        
        if request.user.is_authenticated:
            user=request.user
            create_order=Order(user=user,full_name=full_name,email=email,phone_number=phone_number,shipping_address=shipping_address,amount_paid=amount_paid)
            create_order.save()
            
            order_id=create_order.pk
            for product in cart_products:
                product_id=product.id
                if product.is_sale:
                    price=product.sale_price
                else:
                    price=product.price
                for key,value in quantities().items(): 
                    if int(key) == product.id:
                        create_order_item=OrderItem(order_id=order_id,product_id=product_id,user=user,quantity=value,price=price)
                        create_order_item.save()
                        # delete our cart
            for key in list(request.session.keys()):
                if key=="session_key":
                    del request.session[key]
                    # delete our old cart
                    current_user=Profile.objects.filter(user=request.user)
                    current_user.update(old_cart=" ")
                         
               
                    
                
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('index')
            
        else:
            for key in list(request.session.keys()):
                if key=="session_key":
                    del request.session[key]
            
            messages.success(request, 'You need to login first')
            return redirect('index')
    else:
        messages.success(request, 'You need to login first')
        return redirect('index')

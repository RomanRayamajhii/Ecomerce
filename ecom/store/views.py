from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.forms import Shippingform
from payment.models import ShippingAddress
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_products = Product.objects.filter(
            Q(name__icontains=searched) |
            Q(description__icontains=searched) |
            Q(category__name__icontains=searched)  # Corrected this line
        )
        if not searched_products:
            messages.success(request, 'No product found')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched_products})
    else:
        return render(request, 'search.html', {})
    
def category_summary(request):
    categories=Category.objects.all()
    return render(request, 'category_summary.html', {'categories': categories})
    
def category_view(request, cat):
    cat = cat.replace('-', ' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'category': category, 'products': products})
    except Category.DoesNotExist:
        messages.error(request, 'Category does not exist')
        return redirect('index')

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            current_user = Profile.objects.get(user_id=request.user.id)
            saved_cart= current_user.old_cart
            if saved_cart:
                converted_cart=json.loads(saved_cart)
                cart=Cart(request)
                for key,value in converted_cart.items():
                    product=Product.objects.get(id=int(key))
                    cart.db_add(product=key,quantity=value)
                
                
                
                
            
            
            
            messages.success(request, 'You are successfully logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # Create a Profile object for the new user
            # Profile.objects.create(user=user)
            messages.success(request, 'User created successfully - please fill the user info below..')
            return redirect('update_info')
        else:
            for error in list(form.errors.values()):
                    messages.error(request, error)
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
def update_user(request):
    
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'You  successfully updated your profile')
            return redirect('index')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'You must login to update your profile')
        return redirect('index')
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            pass_form = ChangePasswordForm(current_user, request.POST)
            if pass_form.is_valid():
                pass_form.save()
                messages.success(request, 'You  successfully updated your password')
                # login(request, current_user)
                return redirect('login')
            else:
                for error in list(pass_form.errors.values()):
                    messages.error(request, error)
                return render(request, 'update_password.html', {'pass_form': pass_form})    
        else:
            pass_form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'pass_form': pass_form})
    else:
        messages.success(request, 'You must login to update your password')
        return redirect('home')
def update_info(request):
    if request.user.is_authenticated:
        # Use the `user` field directly in `get_or_create`
        current_user, created = Profile.objects.get_or_create(user=request.user)
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        
        form = UserInfoForm(request.POST or None, instance=current_user)
        Shipping_form = Shippingform(request.POST or None, instance=shipping_user)
        
        if form.is_valid() and Shipping_form.is_valid():
            form.save()
            Shipping_form.save()
            messages.success(request, 'You successfully updated your Info')
            return redirect('index')
        
        return render(request, 'update_info.html', {'form': form, 'Shipping_form': Shipping_form})
    else:
        messages.success(request, 'You must login to update your Info')
        return redirect('index')







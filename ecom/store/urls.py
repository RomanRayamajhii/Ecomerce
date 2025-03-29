from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('login/', views.login_user, name='login'),
   path('register/', views.register_user, name='register'),
   path('logout/', views.logout_user, name='logout'),
   path('update_user/', views.update_user, name='update_user'),
   path('update_password/', views.update_password, name='update_password'),
   path('update_info/', views.update_info, name='update_info'),
   path('product/<int:pk>/', views.product_detail, name='product_details'),
   path('category/<str:cat>/', views.category_view, name='category'),
   path('category_summary', views.category_summary, name='category_summary'),
   path('search/',views.search,name="search"),
   
]

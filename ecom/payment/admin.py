from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
class OrderItemInline(admin.StackedInline):
    model= OrderItem
    extra=0
#extend our order model
class OrderAdmin(admin.ModelAdmin):
    model= Order
    readonly_fields=["date_ordered"]
    fields=["user","full_name","email","phone_number","shipping_address","amount_paid","date_ordered","shipped","date_shipped"]
    
    inlines=[OrderItemInline]
    
    
admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)    

# Register your models here.

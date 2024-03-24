from django.contrib import admin
from offer.models import Category , Offer , Order , OrderItem 


# Register your models here.
admin.site.register(Category) 
admin.site.register(Offer) 
admin.site.register(Order) 
admin.site.register(OrderItem)



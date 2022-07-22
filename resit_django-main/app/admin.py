from django.contrib import admin
from .models import (Customer,Category_choices,Product,Cart,OrderPlaced,Profile)
from django.utils.html import format_html
from django.urls import reverse





@ admin.register(Profile)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','firstname','lastname','phone','address','email','username','profile_pic','created_date']

@ admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','name','address','city','zipcode','province']

@ admin.register(Category_choices)
class Category_choicesModelAdmin(admin.ModelAdmin):
    list_display=['id','title','slug']

@ admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','slug','marked_price','selling_price','brand','description','category','product_image']

@ admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@ admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','profile','customer_info','product_info','product','quantity','ordered_date','status']

    def customer_info(self,obj):
        link=reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)
    
    def product_info(self,obj):
        link=reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
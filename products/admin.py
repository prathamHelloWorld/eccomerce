from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['__str__','slug','product_price']
    list_filter=('slug','product_price')
    pass



# Register your models here.
admin.site.register(Product,ProductAdmin)
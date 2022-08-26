from django.contrib import admin
from .models import Product,ProductImg,Category,Product_Alternative,Product_Accessories
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductImg)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
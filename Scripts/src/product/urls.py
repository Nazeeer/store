
from django.urls import path

from product.views import productlist,productdetail
from . import views
app_name='product'
urlpatterns = [
    path('', productlist , name='product_list'),
    path('<str:slug>',productdetail,name='product_detail'),
    # path('',),
]
from django.urls import path

from .views import signup,profile,profile_edit,signup,order
from . import views
app_name='accounts'
urlpatterns = [
    path('profile',profile,name='profile'),
    path('signup/',signup,name='signup'),
    path('',profile,name='profile'),
    path('order/',order,name='order'),
    path('profile_edit/',profile_edit,name='profile_edit'),
    # path('profile/signup/',signup,name='profile_signup'),
]
from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('cartdetail', views.cartdetailview.as_view(), name='cartdetail'),
    path('addproduct', views.addproduct.as_view(), name='addproduct'),
]
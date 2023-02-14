from . import views
from django.urls import path


app_name='cart'
urlpatterns = [
    path('', views.cart_details, name='cart_detailscart_details'),
]
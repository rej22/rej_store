from . import views
from django.urls import path

app_name = 'rej_home'
urlpatterns = [
    path('', views.allProducts, name='allProducts'),
    path('<slug:category_slug>/', views.allProducts, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.productDetails, name='productDetails'),
]

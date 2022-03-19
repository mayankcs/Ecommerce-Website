from django.urls import path
from . import views


urlpatterns = [
    path('addToCart/<int:pk>/', views.addToCart, name='addToCart'),
    path('purchase/<int:pk>/', views.purchase, name='purchase'),
    path('purchaseall/', views.purchaseAll, name='purchaseAll'),
    path('mycart/', views.mycart, name='mycart'),
    path('myorders/', views.myorders, name='myorders'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:pk>/', views.checkout2, name='checkout'),
    path('removefromcart/<int:pk>/', views.removefromcart, name='removefromcart'),
    path('sellersells/', views.sellersells, name='sellersells'),
]




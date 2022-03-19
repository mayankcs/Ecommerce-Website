from django.urls import path
from . import views


urlpatterns = [
    path('addProduct/', views.addProduct, name='add_Product'),
    path('home', views.home, name='home'),
    path('homedetail/<int:pk>/', views.homedetail, name='homedetail'),
    path('updateproduct/<int:pk>/', views.updateproduct, name='updateproduct'),
    path('removeproduct/<int:pk>/', views.removeproduct, name='removeproduct'),
]




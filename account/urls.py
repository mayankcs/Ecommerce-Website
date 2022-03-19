from django.urls import path
from . import views

urlpatterns = [
    path('roll/', views.roll, name='roll'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/<int:pk>/', views.register, name='register'),
    path('sellerProfile/', views.sellerProfile, name='sellerProfile'),
    path('thrtry/', views.thrtry, name='thrtry'),
]

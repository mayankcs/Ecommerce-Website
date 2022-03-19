from django.shortcuts import render, HttpResponse,redirect
from account.models import seller

def allowedUser():
    def allowedUserdecorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            if seller.objects.filter(seller_username__id=request.user.id):
                print("wooowo")
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("User must be seller for selling")
        return wrapper_func
    return allowedUserdecorator


def isAuthenticated_decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            if request.user.is_authenticated:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("User must logged in to perform this action")
        return wrapper_func
   
  
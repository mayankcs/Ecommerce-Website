from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from .models import customer,seller
from product.decorator import allowedUser
from product.models import product

def roll(request):
    return render (request, 'accounts/roll.html')

def register(request,pk):   
    if request.method == 'POST':
        print("yesssssss")  
        first_name,last_name,phone_number="","",""   
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                msg1="username taken"
                return redirect('/account/register',{'msg': msg1,'pk':pk})
                #return HttpResponse(msg1)
                #return render(request, 'accounts/register.html', {'msg': msg1})

            else:
                user=User.objects.create_user(username=username,password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                if pk==1:
                    
                    phone_number = request.POST['phone_number']
                    ccustomer, created = customer.objects.get_or_create(customer_username=user, phone_number=phone_number)
                    #custmor created
                    return redirect('/account/login')
                    #return render(request, 'accounts/login.html')
                else:
                    shop_name, phone_number, address, apartment, city, state="","","","","",""
                    shop_name = request.POST['shop_name']
                    phone_number = request.POST['phone_number']
                    address = request.POST['address']
                    apartment = request.POST['apartment']
                    city = request.POST['city']
                    state = request.POST['state']
                    pincode = request.POST['pincode']
                    sseller, created = seller.objects.get_or_create(seller_username=user, shop_name=shop_name,phone_number=phone_number,address=address,apartment=apartment,city=city,state=state,pincode=pincode)
                    print("Seller is created")
                    return redirect('/account/login')
        else :
            msg="Password not same"
            return render(request, 'accounts/register.html',{'msg':msg,'pk':pk})
    else:
        
        return render(request, 'accounts/register.html', {'pk':pk})


def login(request):
    try:
        
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user=auth.authenticate(username=username,password=password )
            if user is not None:
                auth.login(request, user)
                if (seller.objects.filter(seller_username__id=request.user.id)).exists():
                    return HttpResponseRedirect("/account/sellerProfile")
                else:
                    return HttpResponseRedirect("/product/home")
            else :
                msg="invalid details"
                return render(request, 'accounts/login.html' ,{'msg':msg})
        else:
            return render(request, 'accounts/login.html' )
        # else:
        #     return HttpResponseRedirect("/account/sellerProfile")
    except:
        return HttpResponse("something went wrong , please go back")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/account/login")

@allowedUser()
def sellerProfile(request):
    user=request.user.id
    seller_obj=seller.objects.get(seller_username__id=user)
    product_obj=product.objects.filter(seller__id=seller_obj.id)[::-1]
    msg=True
    if (product_obj):
        msg=False 
    context={'seller_obj':seller_obj,'product_obj':product_obj,'msg':msg}
    return render(request, 'accounts/sellerprofile.html',context )



def thrtry(request):
    print()
    return HttpResponse("hello")
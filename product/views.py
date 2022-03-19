from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from .decorator import allowedUser
from .models import product,category
from account.models import seller
from django.core.files.storage import FileSystemStorage
# Create your views here.

@allowedUser()
def addProduct (request):
    data=""
    if request.method == 'POST':
        seller_id=seller.objects.get(seller_username__id=request.user.id)
        name = request.POST['name']
        cat = request.POST['cat']
        catdata=category.objects.get(id=cat)
        imagee = request.FILES['image']
        imformation = request.POST['imformation']
        quantity = request.POST['quantity']
        price = request.POST['price']
        pproduct= product(seller=seller_id, name=name,category=catdata,image=imagee,imformation=imformation,quantity=quantity,price=price)
        pproduct.save()
    
        return redirect('/account/sellerProfile')
        #return HttpResponse("product added")
    else :
        data=category.objects.all()
        context={'data':data}
        return render (request , 'product/addproduct.html',context)
       
def updateproduct(request,pk):
    if request.method == 'POST':
        name = request.POST['name']
        cat = request.POST['cat']
        catdata=category.objects.get(name=cat)
        #imagee = request.FILES['image']
        imformation = request.POST['imformation']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product_update=product.objects.filter(id=pk).update(name=name,category=catdata,imformation=imformation,quantity=quantity,price=price)
        return HttpResponseRedirect("/account/sellerProfile")
    else:
        p_data=product.objects.get(id=pk)
        c_data=category.objects.all()
        context={'p_data':p_data,'c_data':c_data}
        return render (request , 'product/updateproduct.html',context)

def removeproduct(request,pk):
    product.objects.filter(id=pk).delete()
    return HttpResponseRedirect("/account/sellerProfile")
           
def home(request):
    flag=False
    try:
        if seller.objects.get(seller_username__id=request.user.id):
            flag=True
            
    except:
        pass
    
    user=False
    if request.user.is_authenticated:
        user=request.user.username
    products=product.objects.all()
    context={'products':products,'user':user,'flag':flag}
    return render (request , 'product/homepage.html',context)
    

def homedetail(request,pk):
    user=request.user
    products=product.objects.get(id=pk)
    context={'products':products}
    return render (request , 'product/productDetail.html',context)


from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import cart,purchased
from product.models import product
from account.models import customer,seller
from product.decorator import isAuthenticated_decorator,allowedUser

#       cart        view


@isAuthenticated_decorator  
def addToCart(request,pk):   
    cust=customer.objects.get(customer_username__id=request.user.id)
    products=product.objects.get(id=pk)
    seller=products.seller   
    pcart= cart(user_id=cust,seller_id=seller,product_id=products)
    pcart.save()
    # return HttpResponse("item added to cart")
    return HttpResponseRedirect("/cart/mycart")

@isAuthenticated_decorator  
def mycart(request):  
    username=request.user.username
    cust=customer.objects.get(customer_username__id=request.user.id)
    mycart_data=cart.objects.filter(user_id=cust.id)
    context={'mycart':mycart_data,'username':username}
    return render(request,'cart/myCart.html',context)

@isAuthenticated_decorator  
def myorders(request):  
    username=request.user.username
    cust=customer.objects.get(customer_username__id=request.user.id)
    purchased_data=purchased.objects.filter(user_id=cust.id)[::-1]
    context={'purchased':purchased_data,'username':username}
    return render(request,'cart/myPurchase.html',context)

#       purhcasing      view

@isAuthenticated_decorator    
def purchase(request,pk):
    sellers_obj=""
    cust=customer.objects.get(customer_username__id=request.user.id) #customer object
    products=product.objects.get(id=pk) # product object
    sellers_obj=products.seller # seller object
    if products.quantity > 0 :
        #creating purchase object   
        ppurchased= purchased(user_id=cust,seller_id=sellers_obj,product_id=products)
        ppurchased.save()
        # decrease quantity by 1
        products_quantity=products.quantity - 1
        quanitity=product.objects.filter(id=pk).update(quantity=products_quantity)
        #now add cash to seller earnings
        t_earn=(sellers_obj.total_earning) + (products.price)
        seller_earnings=seller.objects.filter(id=sellers_obj.id).update(total_earning=t_earn)
        #now delete the object from cart
        if cart.objects.filter(product_id__id=pk):
            cart.objects.get(product_id__id=pk).delete()
        return HttpResponseRedirect("/cart/myorders")
    else:
        return HttpResponse("Item out of stock")

@isAuthenticated_decorator 
def checkout(request):
    username=request.user.username
    cust=customer.objects.get(customer_username__id=request.user.id)
    mycart_data=cart.objects.filter(user_id=cust.id)

    total=0
    quantity=0
    for i in mycart_data:
        total+=i.product_id.price
        quantity+=1
    context={'mycart':mycart_data,'username':username,'total':total,'quantity':quantity}
    return render (request , 'cart/checkout.html',context)

def purchaseAll(request):
    username=request.user.username
    cust=customer.objects.get(customer_username__id=request.user.id)
    mycart_data=cart.objects.filter(user_id=cust.id)
    # all wala logic starts here
    for cartProduct in mycart_data:
        sellers_obj=cartProduct.seller_id # seller object
        products=cartProduct.product_id # product object
        if products.quantity > 0 :
            #creating purchase object   
            ppurchased= purchased(user_id=cust,seller_id=sellers_obj,product_id=products)
            ppurchased.save()
            # decrease quantity by 1
            products_quantity=products.quantity - 1
            quanitity=product.objects.filter(id=cartProduct.product_id.id).update(quantity=products_quantity)
            #now add cash to seller earnings
            t_earn=(sellers_obj.total_earning) + (products.price)
            seller_earnings=seller.objects.filter(id=sellers_obj.id).update(total_earning=t_earn)
            #now delete the object from cart 
            cart.objects.filter(product_id__id=products.id).delete()
        else:
            return HttpResponse("Item out of stock")
    return HttpResponseRedirect("/cart/myorders")
        
        
    

@isAuthenticated_decorator 
def checkout2(request,pk):
    data=product.objects.get(id=pk)
    context={'mycart':data}
    return render (request , 'cart/checkout2.html',context)

def removefromcart(request,pk):
    cart.objects.filter(product_id__id=pk).delete()
    return HttpResponseRedirect("/cart/mycart")

@allowedUser()
def sellersells(request):
    seller_obj=seller.objects.get(seller_username__id=request.user.id)
    products_sold=purchased.objects.filter(seller_id=seller_obj.id)[::-1]
    print(products_sold)
    context={'products_sold':products_sold}
    return render (request , 'cart/sellerSells.html',context)
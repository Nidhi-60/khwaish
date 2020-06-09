from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from datetime import datetime
from django.contrib.auth.models import User
from django.apps import apps
from django.http import HttpResponse

# Create your views here.

# get product model
product = apps.get_model('Artists', 'Artistpainting')
artist = apps.get_model('Artists', 'Artist')
paintingcategory = apps.get_model('Artists', 'Paintingcategory')
paintingsofcategory = apps.get_model('Artists', 'Paintingofcategory')
userdetail = apps.get_model('Accounts', 'Userdetail')

# artist Navbar
def artistname():
    artistname = artist.objects.all()
    return artistname


# category Navbar
def category():
    catgoryname = paintingcategory.objects.all()
    return catgoryname



# add to cart
@login_required(login_url='login')
def cart(request, pid, code):
       user = User.objects.get(id=request.user.id)
       cartmodel = models.Cart()
       cartmodel.user = user
       if code == 'A':
           cartmodel.artistproduct = product.objects.get(id=pid)
           cartmodel.categoryproduct = None
       else:
           cartmodel.categoryproduct = paintingsofcategory.objects.get(id=pid)
           cartmodel.artistproduct = None
       cartmodel.cartdate = datetime.now()
       cartmodel.save()
       return redirect('home')


# count sum
def counttotal(userid):
    count = {}
    sum = 0
    cart = models.Cart.objects.filter(user=userid)
    for i in cart:
        if i.artistproduct is None:
            count[i.categoryproduct.paintingname] = i.categoryproduct.paintingprice
            # count.append(i.categoryproduct.paintingprice)
            sum += int(i.categoryproduct.paintingprice)
        else:
            count[i.artistproduct.paintingname] = i.artistproduct.paintingprice
            # count.append(i.artistproduct.paintingprice)
            sum += int(i.artistproduct.paintingprice)
    print(count)
    count['Total'] = sum
    return count


# cartdetail
# still remaining if user detail not exists then msg = edit detail
@login_required(login_url='login')
def cartdetail(request):
    userdata = userdetail.objects.get(user=request.user.id)
    print(userdata)
    count = counttotal(request.user.id)
    print(count)
    artistnavname = artistname()
    categoryname = category()
    cart = models.Cart.objects.filter(user=request.user.id)
    cartitem = models.Cart.objects.filter(user=request.user.id)
    if len(cartitem) == 0:
        context = {
            'artistnavname': artistnavname,
            'categoryname': categoryname,
            'error': "Cart is empty",
            'userdata': userdata
        }
        template = 'order_temp/cartdetail.html'
        return render(request, template_name=template, context=context)
    else:
        productdetail = []
        product = []
        for i in cart:
            productdetail.append(i)
        for j in productdetail:
            product.append(j)
        context = {
            'artistnavname': artistnavname,
            'categoryname': categoryname,
            'cart': cart,
            'product': productdetail,
            'cartitem': len(cartitem),
            'count': count,
            'userdata': userdata

        }
        template = 'order_temp/cartdetail.html'
        return render(request, template_name=template, context=context)


# remove cart detail
def remove(request, pid, code):
    if code == 'C':
        cart = models.Cart.objects.get(categoryproduct=pid)
    else:
        cart = models.Cart.objects.get(artistproduct=pid)
    cart.delete()
    return redirect('cartdetail')

# final price
def price(userid):
    count = {}
    sum = 0
    cart = models.Buy.objects.filter(user=userid)
    for i in cart:
        if i.artistproduct is None:
            count[i.categoryproduct.paintingname] = i.categoryproduct.paintingprice
            # count.append(i.categoryproduct.paintingprice)
            sum += int(i.categoryproduct.paintingprice)
        else:
            count[i.artistproduct.paintingname] = i.artistproduct.paintingprice
            # count.append(i.artistproduct.paintingprice)
            sum += int(i.artistproduct.paintingprice)
    print(count)
    count['Total'] = sum
    return sum


# buy all product from the cart
def buy(request, uid):
    buydata = models.Buy.objects.all()
    totalbuyers = len(buydata)
    cart = models.Cart.objects.filter(user=uid)
    artistnavname = artistname()
    categoryname = category()
    for i in cart:
        buydetail = models.Buy()
        buydetail.user = i.user
        if i.artistproduct is None:
            buydetail.categoryproduct = i.categoryproduct
        else:
            buydetail.artistproduct = i.artistproduct
        buydetail.status = 'pending'
        buydetail.buydate = datetime.now()
        buydetail.orderid = totalbuyers
        buydetail.save()
        if i.artistproduct is None:
            remove(request, i.categoryproduct.id, i.categoryproduct.paintingcode)
        else:
            remove(request, i.artistproduct.id, i.artistproduct.paintingcode)
    userbuydata = models.Buy.objects.filter(user=request.user.id)
    print(userbuydata)
    finalprice = price(request.user.id)
    context = {
       'message': 'Your order Has been submitted...',
       'userbuydata': userbuydata,
        'finalprice': finalprice,
        'artistnavname': artistnavname,
        'categoryname': categoryname,
    }
    template = 'order_temp/buy.html'
    return render(request, template_name=template, context=context)


# display buy detail after click buy from the cart



# single buy from the Pages
@login_required(login_url='login')
def buynow(request, pid, code):
    buydata = models.Buy.objects.all()
    totalbuyers = len(buydata)
    buydetil = models.Buy()
    artistnavname = artistname()
    categoryname = category()
    if code == 'A':
        buydetil.user = User.objects.get(id=request.user.id)
        buydetil.artistproduct = product.objects.get(id=pid)
        buydetil.status = 'pending'
        buydetil.buydate = datetime.now()
        buydetil.orderid = totalbuyers
        buydetil.save()
        print('done A')
    else:
        buydetil.user = User.objects.get(id=request.user.id)
        buydetil.categoryproduct = paintingsofcategory.objects.get(id=pid)
        buydetil.status = 'pending'
        buydetil.buydate = datetime.now()
        buydetil.orderid = totalbuyers
        print('done B')
    userbuydata = models.Buy.objects.filter(user=request.user.id)
    print(userbuydata)
    finalprice = price(request.user.id)
    context = {
        'message': 'Your order Has been submitted...',
        'userbuydata': userbuydata,
        'finalprice': finalprice,
        'artistnavname': artistnavname,
        'categoryname': categoryname,
    }
    template = 'order_temp/buy.html'
    return render(request, template_name=template, context=context)


# single buy from the cart
def buynowcart(request, pid, code):
    buydata = models.Buy.objects.all()
    totalbuyers = len(buydata)
    buydetil = models.Buy()
    artistnavname = artistname()
    categoryname = category()
    if code == 'A':
        buydetil.user = User.objects.get(id=request.user.id)
        buydetil.artistproduct = product.objects.get(id=pid)
        buydetil.status = 'pending'
        buydetil.buydate = datetime.now()
        buydetil.save()
        buydetil.orderid = totalbuyers
        remove(request, pid, code)
        print('done A')
    else:
        buydetil.user = User.objects.get(id=request.user.id)
        buydetil.categoryproduct = paintingsofcategory.objects.get(id=pid)
        buydetil.status = 'pending'
        buydetil.buydate = datetime.now()
        buydetil.orderid = totalbuyers
        remove(request, pid, code)
        print('done B')
    userbuydata = models.Buy.objects.filter(user=request.user.id)
    print(userbuydata)
    finalprice = price(request.user.id)
    context = {
        'message': 'Your order Has been submitted...',
        'userbuydata': userbuydata,
        'finalprice': finalprice,
        'artistnavname': artistnavname,
        'categoryname': categoryname,
    }
    template = 'order_temp/buy.html'
    return render(request, template_name=template, context=context)


# success Page
def success(request):
    context = {
        'message': "Your Order Has Been Submitted..",
        'message1': "We Will Notify After Confirm Your Order..",
    }
    template = 'order_temp/success.html'
    return render(request, template_name=template, context=context)
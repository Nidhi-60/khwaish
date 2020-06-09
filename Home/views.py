from django.shortcuts import render
from django.apps import apps
from django.core import serializers
from django.http import HttpResponse
from random import sample

# Create your views here.

artist = apps.get_model('Artists', 'Artist')
painting = apps.get_model('Artists', 'Artistpainting')
paintingcategory = apps.get_model('Artists', 'Paintingcategory')
paintingofcategory = apps.get_model('Artists', 'Paintingofcategory')
paintings = apps.get_model('Artists', 'Paintingofcategory')
cartmodel = apps.get_model('Orders', 'Cart')


# artist Navbar
def artistname():
    artistname = artist.objects.all()
    return artistname


# category Navbar
def category():
    catgoryname = paintingcategory.objects.all()
    return catgoryname


# cartdetail
def cartcount(userid):
    cart = cartmodel.objects.filter(user=userid)
    return cart


# home page
def home(request):
    # print(dir(request))
    cart = cartcount(request.user.id)
    artistnavname = artistname()
    categoryname = category()
    artistdetail = sample(list(artist.objects.all()), 3)
    categorytype = sample(list(paintingcategory.objects.all()), 3)
    context = {
       'artistnavname': artistnavname,
       'artistdetail': artistdetail,
       'categoryname': categoryname,
       'categorytype': categorytype,
        'cartitem': len(cart)
    }
    template = 'home_temp/home.html'

    return render(request, template_name=template, context=context)


# search Painting
def searchpainting(request, key):
    paint = painting.objects.filter(paintingname__icontains=key)
    painting_list = serializers.serialize('json', paint)
    return HttpResponse(painting_list, content_type='text/json-comment-filtered')




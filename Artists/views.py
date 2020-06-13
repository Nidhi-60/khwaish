from django.shortcuts import render
from . import models
from django.apps import apps
from .Reviewform import Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

# get model
cartmodel = apps.get_model('Orders', 'Cart')
reviewmodel = apps.get_model('Blogs', 'Review')


# cartdetail
def cartcount(userid):
    cart = cartmodel.objects.filter(user=userid)
    return cart


# paiting by artist id
def paintingbyartist(request, artistid):
    cart = cartcount(request.user.id)
    artistnavname = models.Artist.objects.all()
    categoryname = models.Paintingcategory.objects.all()
    paintings = models.Artistpainting.objects.filter(artist=artistid)
    artistdetail = models.Artist.objects.get(id=artistid)
    p = Paginator(paintings, 3)
    page_number = request.GET.get('page')
    if page_number:
        current_page = p.get_page(page_number)
    else:
        current_page = p.get_page(1)
    context = {
        'painting': paintings,
        'artistnavname': artistnavname,
        'artistdetail': artistdetail,
        'categoryname': categoryname,
        'cartitem': len(cart),
        'a_page': current_page
    }
    template = 'artist_temp/paintingbyartist.html'

    return render(request, template_name=template, context=context)


# artist painting detail
@login_required(login_url='login')
def paintingdetail(request, paintingid):
    cart = cartcount(request.user.id)
    artistnavname = models.Artist.objects.all()
    categoryname = models.Paintingcategory.objects.all()
    paintings = models.Artistpainting.objects.get(id=paintingid)
    reviewform = Review(request.POST or None)
    if reviewform.is_valid():
        obj = reviewform.save(commit=False)
        obj.user = request.user
        obj.artist = paintings
        obj.category = None
        reviewform.save(commit=True)
    allreview = reviewmodel.objects.filter(artist=paintingid)
    contex = {
      'artistnavname': artistnavname,
      'paintings': paintings,
      'categoryname': categoryname,
        'cartitem': len(cart),
        'form': reviewform,
        'review': allreview,
    }
    template = 'artist_temp/paintingdetail.html'

    return render(request, template_name=template, context=contex)


# painting by category id
def paintingbycategory(request, categoryid):
    cart = cartcount(request.user.id)
    artistnavname = models.Artist.objects.all()
    categoryname = models.Paintingcategory.objects.all()
    categorynames = models.Paintingcategory.objects.get(id=categoryid)
    paintingsbycategory = models.Paintingofcategory.objects.filter(categoryid=categoryid)
    print(categoryid)
    p = Paginator(paintingsbycategory, 3)
    page_number = request.GET.get('page')
    if page_number:
        current_page = p.get_page(page_number)
    else:
        current_page = p.get_page(1)
    context = {
        'artistnavname': artistnavname,
        'categoryname': categoryname,
        'paintingsbycategory': paintingsbycategory,
        'categorynames': categorynames,
        'cartitem': len(cart),
        'a_page': current_page
    }

    template = 'artist_temp/paintingbycategory.html'
    return render(request, template_name=template, context=context)


# category wise painting with detail
def categorydetail(request, paintingid):
    cart = cartcount(request.user.id)
    artistnavname = models.Artist.objects.all()
    categoryname = models.Paintingcategory.objects.all()
    painting = models.Paintingofcategory.objects.get(id=paintingid)
    reviewform = Review(request.POST or None)
    if reviewform.is_valid():
        obj = reviewform.save(commit=False)
        obj.user = request.user
        obj.artist = None
        obj.category = painting
        reviewform.save(commit=True)
    allreview = reviewmodel.objects.filter(category=paintingid)
    context = {
        'artistnavname': artistnavname,
        'categoryname': categoryname,
        'painting': painting,
        'cartitem': len(cart),
        'form': reviewform,
        'review': allreview,
    }

    template = 'artist_temp/categorypaintingdetail.html'

    return render(request, template_name=template, context=context)
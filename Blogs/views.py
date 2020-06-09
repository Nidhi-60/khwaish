from django.shortcuts import render, redirect
from django.apps import apps
from .models import ArtistBlog, Feedback, Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime

# getmodel
artist = apps.get_model('Artists', 'Artist')
paintingcategory = apps.get_model('Artists', 'Paintingcategory')
cartmodel = apps.get_model('Orders', 'Cart')
categorypainting = apps.get_model('Artists', 'Paintingofcategory')
artistpaintig = apps.get_model('Artists', 'Artistpainting')


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

# Create your views here.


# Artist blog
def artistblog(request, aid):
    artistnavname = artistname()
    categoryname = category()
    cart = cartcount(request.user.id)
    artistdetail = ArtistBlog.objects.get(id=aid)
    context = {
        'artistnavname': artistnavname,
        'categoryname': categoryname,
        'cartitem': len(cart),
        'artist': artistdetail
    }
    template = 'blog_temp/artistblog.html'
    return render(request, template_name=template, context=context)


# artists Blog
def artistsblog(request):
    artistnavname = artistname()
    categoryname = category()
    cart = cartcount(request.user.id)
    artistdetail = ArtistBlog.objects.all()
    context = {
        'artistnavname': artistnavname,
        'categoryname': categoryname,
        'cartitem': len(cart),
        'artists': artistdetail
    }
    template = 'blog_temp/artistsblog.html'
    return render(request, template_name=template, context=context)


# feedback
@login_required(login_url='login')
def feedback(request):
    if request.method == 'POST':
        if request.POST['txtfeedback'] == '':
            artistnavname = artistname()
            categoryname = category()
            cart = cartcount(request.user.id)
            context = {
                'artistnavname': artistnavname,
                'categoryname': categoryname,
                'cartitem': len(cart),
                'error': 'Please Fill The Field'
            }
            template = 'blog_temp/feedback.html'
            return render(request, template_name=template, context=context)
        else:
            fb = Feedback()
            fb.user = User.objects.get(id=request.user.id)
            fb.feedback = request.POST['txtfeedback']
            fb.save()
            return redirect('home')
    else:
        artistnavname = artistname()
        categoryname = category()
        cart = cartcount(request.user.id)
        context = {
            'artistnavname': artistnavname,
            'categoryname': categoryname,
            'cartitem': len(cart),
        }
        template = 'blog_temp/feedback.html'
        return render(request, template_name=template, context=context)


# Remove Reviews
def reviewremove(request, rid, pid):
    review = Review.objects.get(id=rid)
    review.delete()
    if review.artist is not None:
        return redirect('paintingdetail', paintingid=pid)
    else:
        return redirect('categorypaintingdetail', paintingid=pid)




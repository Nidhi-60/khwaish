from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.apps import apps
from .models import Userdetail
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse

# Create your views here.

artist = apps.get_model('Artists', 'Artist')
paintingcategory = apps.get_model('Artists', 'Paintingcategory')
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


# send mail
def mail(email, username):
    sender = 'khwaishartgallary@gmail.com'
    receiver = email
    password = 'art@khwaish123'

    message = EmailMessage()
    message['Subject'] = "Khwaish Art Gallary"
    message['From'] = sender
    message['To'] = receiver
    msg = f"<h4 style='font-family:Kozuka Mincho Pr6N;font-size: 12px;'> " \
            f"Dear , {username} <br> You Have Just Sign in to Khwaish Art Gallary " \
            f"<br><br><br> Your sincerely , <br> Khwaish Art Gallary </h4>"
    message.set_content(msg, subtype='html')

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login(sender, password)
        mail.send_message(message)
        print("Email sent..")
    except smtplib.SMTPException as e:
        print(e)


# signup page
def signup(request):
    cart = cartcount(request.user.id)
    artistnavname = artistname()
    categoryname = category()
    if request.method == 'POST':
        if request.POST['txtusername'] == "" or request.POST['txtpassword'] == "" or request.POST['txtrepassword'] == "" or request.POST['txtemail'] == "":
            return render(request, 'account_temp/signup.html', {'error': 'Please fill the fields', 'artistnavname':artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})
        else:
            if request.POST['txtpassword'] == request.POST['txtrepassword']:
                try:
                    user = User.objects.get(username=request.POST['txtusername'])
                    if user is not None:
                        return render(request, 'account_temp/signup.html', {'error': 'User Already exists', 'artistnavname':artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})
                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['txtusername'], email=request.POST['txtemail'], password=request.POST['txtpassword'])
                    auth.login(request, user)
                    mail(request.POST['txtemail'], request.POST['txtusername'])
                    return redirect('user')
            else:
                return render(request, 'account_temp/signup.html', {'error': 'Password Not match.', 'artistnavname':artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})
    else:
        return render(request, 'account_temp/signup.html', {'artistnavname': artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})


# login page
def login(request):
    cart = cartcount(request.user.id)
    artistnavname = artistname()
    categoryname = category()
    if request.method == 'POST':
        if request.POST['txtusername'] == '' or request.POST['txtpassword'] == '':
            return render(request, 'account_temp/login.html', {'error': 'Please Fill the field', 'artistnavname': artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})
        else:
            user = auth.authenticate(username=request.POST['txtusername'], password=request.POST['txtpassword'])
            if user is not None:
                auth.login(request, user)
                if request.POST['txtnextpage']:
                    return redirect(request.POST['txtnextpage'])
                else:
                    return redirect('home')
            else:
                return render(request, 'account_temp/login.html', {'error': 'Username or Password not match', 'artistnavname': artistnavname, 'categoryname': categoryname, 'cartitem': len(cart)})
    else:
        return render(request, 'account_temp/login.html', {'artistnavname': artistnavname, 'categoryname': categoryname,'cartitem': len(cart)})


# userdetail
def userdetail(request):
    artistnavname = artistname()
    categoryname = category()
    try:
        userdata = Userdetail.objects.get(user=request.user.id)
        if userdata is not None:
            if request.method == 'POST':
                userdata.user = User.objects.get(id=request.user.id)
                userdata.address = request.POST['txtaddress']
                userdata.pincode = request.POST['txtpincode']
                userdata.city = request.POST['txtcity']
                userdata.state = request.POST['txtstate']
                userdata.save()
                return redirect('home')
            else:
                context = {
                    'artistnavname': artistnavname,
                    'categoryname': categoryname,
                    'userdata': userdata
                }
                template = 'account_temp/userdetail.html'
                return render(request, template_name=template, context=context)
        else:
            if request.method == 'POST':
                if request.POST['txtaddress'] == '' or request.POST['txtpincode'] == '' or request.POST['txtcity'] == '' \
                        or request.POST['txtstate'] == '':
                    context = {
                        'error': 'Please Fill the field'
                    }
                    template = 'account_temp/userdetail.html'
                    return render(request, template_name=template, context=context)
                else:
                    user = Userdetail()
                    user.user = request.user
                    user.adrress = request.POST['txtaddress']
                    user.pincode = request.POST['txtpincode']
                    user.city = request.POST['txtcity']
                    user.state = request.POST['txtstate']
                    user.save()
                    return redirect('home')
            else:
                artistnavname = artistname()
                categoryname = category()
                context = {
                    'artistnavname': artistnavname,
                    'categoryname': categoryname,
                }
                template = 'account_temp/userdetail.html'
                return render(request, template_name=template, context=context)
    except ValueError as e:
        return HttpResponse(e)


# logout
def logout(request):
    auth.logout(request)
    return redirect('home')
from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:pid>/<str:code>/', views.cart, name='cart'),
    path('cart/', views.cartdetail, name='cartdetail'),
    path('remove/<int:pid>/<str:code>/', views.remove, name='remove'),
    path('buy/<int:uid>/', views.buy, name='buy'),
    path('buynow/<int:pid>/<str:code>', views.buynow, name='buynow'),
    path('buynowcart/<int:pid>/<str:code>', views.buynowcart, name='buynowcart'),
    path('success/', views.success, name='success'),
]
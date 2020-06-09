from django.urls import path
from . import views

urlpatterns = [
    path('<int:artistid>/', views.paintingbyartist, name='artistpainting'),
    path('painting/<int:paintingid>/', views.paintingdetail, name='paintingdetail'),
    path('category/<int:categoryid>/', views.paintingbycategory, name='categorypainting'),
    path('categorypainting/<int:paintingid>/', views.categorydetail, name='categorypaintingdetail'),
]
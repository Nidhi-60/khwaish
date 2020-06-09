from django.urls import path
from . import views

urlpatterns = [
    path('', views.artistsblog, name='blog'),
    path('<int:aid>', views.artistblog, name='artistblog'),
    path('feedback/', views.feedback, name='feedback'),
    path('review/delete/<int:rid>/<int:pid>/', views.reviewremove, name='removereview'),
]
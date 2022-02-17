from django.urls import path, include
from django.shortcuts import render, redirect 
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('', views.signIn, name="login"),
    path('app/', views.app, name='app'),
    path('postsignIn/', views.postsignIn), 

    path('signUp/', views.signUp, name="signup"), 
    path('logout/', views.logout, name="log"), 
    path('postsignUp/', views.postsignUp), 
    path('buy-portal/', views.buy_portal),
    path('about/',views.about,name="about"),
]
from django.contrib import admin
from django.urls import path 
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("product",views.product,name='product'),
    path("view/<int:pk>/",views.view,name = 'view'),
    path("Contact",views.Contact,name='Contact'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("Logout",views.Logout,name='Logout'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("welcome",views.welcome,name='welcome'),
]

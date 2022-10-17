from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("categories",views.categories, name="categories"),
    path("categories/<int:id>", views.categories_choose, name="categories_choose"),
   
    
]
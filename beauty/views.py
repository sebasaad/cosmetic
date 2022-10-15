from audioop import reverse
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from sqlite3 import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  redirect

from .models import User, Category, Product

# Create your views here.





def index(request):
    activeProduct = Product.objects.filter(isActive=True)
    return render(request, "beauty/index.html",{
        "products": activeProduct
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "beauty/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "beauty/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "beauty/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "beauty/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "beauty/register.html")




        
def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "beauty/create.html",{
            "categories": allCategories
        })
    else:
        productName = request.POST["productName"]
        informaton = request.POST["information"]
        image = request.POST["image"]
        price = request.POST["price"]
        category = request.POST["category"]
        categoryData = Category.objects.filter(id=category).first()
        
        
        newListing = Product(
            productName=productName,
            information=informaton,
            image=image, 
            price=price,
            category=categoryData,
            
        )
        newListing.save()
        return redirect(index)


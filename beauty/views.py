from audioop import reverse
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from sqlite3 import IntegrityError
from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  redirect

from .models import User, Category, Product

# Create your views here.



def search(request):
    pro = Product.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            pro = pro.filter(productName__icontains=name)

        context = {
            'products':pro
        }
        return render(request, 'beauty/search.html', context)
    return render(request, 'beauty/search.html', {'products': pro})
"""


def search(request):        
    if request.method == 'POST':      
        searchname =  request.POST.getlist('search')      
        try:
            status = Add_prod.objects.filter(productName__icontains=searchname)
            #Add_prod class contains a column called 'bookname'
        except Add_prod.DoesNotExist:
            status = None
        return render(request,"search.html",{"product":status})
    else:
        return render(request,"search.html",{})


"""

def categories(request):
    auctions = Product.objects.all()
    return render(request, "beauty/categories.html",{
        "categories":Category.objects.all(),
        "products" : auctions,
    })



def categories_choose(request, id):
    auctions_by_cat = Product.objects.filter(category_id= id)
    return render(request, "beauty/categories.html",{
        "products" : auctions_by_cat,
        "categories" : Category.objects.all(),
    })

def index(request):
    activeProduct = Product.objects.filter(isActive=True)
    return render(request, "beauty/index.html",{
        "products": activeProduct
    })
    
def addWatchlist(request, id):
    listingData=Product.objects.get(pk=id)
    currentuser=request.user
    listingData.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse("index",args=(id, )))
    
def addCart(request, id):
    listingData=Product.objects.get(pk=id)
    currentuser=request.user
    listingData.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse("index",args=(id, )))    

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
        


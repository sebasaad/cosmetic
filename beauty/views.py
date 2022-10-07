from audioop import reverse
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.





def index(request):
 
    return render(request, "beauty/index.html")

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
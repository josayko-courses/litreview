from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("feed")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("feed")
        else:
            messages.error(request, "Username or password does not exist")

    context = {"title": "Login", "page": page}
    return render(request, "accounts/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("feed")


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("feed")
        else:
            messages.error(request, "An error occurred during registration")

    context = {"title": "Sign Up", "form": form}
    return render(request, "accounts/login_register.html", context)

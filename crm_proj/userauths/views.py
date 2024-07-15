from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm

# Create your views here.


def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"A user with the username '{username}' has been created successfully.")
            return redirect("userauths:login")

    context = {"form": form}
    return render(request, "userauths/signup.html", context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("core:home")
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, 'userauths/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out. Come back soon!")
    return redirect("userauths:register")

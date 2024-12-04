from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.form.forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.#


def register_request(request):
    if request.method == "POST":
        _mutable = request.POST._mutable
        request.POST._mutable = True
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return render(request, 'forms/auth/login.html')
        else:
            messages.error(request, form.errors)
            return render(request, 'forms/auth/register.html')
    messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'forms/auth/register.html')

def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/dashboard")
    return render(request, 'forms/auth/login.html')

def register_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/dashboard")
    return render(request, 'forms/auth/register.html')


def login_request(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/dashboard")
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("/dashboard")
        else:
            messages.error(request,"Invalid Credentials")
            return render(request, "forms/auth/login.html")
    else:
        messages.error(request,"Error in Form Submission")
        return render(request, "forms/auth/login.html")


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("/")


def forgot_password_view(request):
    return render(request, 'forms/auth/reset_password_form.html')

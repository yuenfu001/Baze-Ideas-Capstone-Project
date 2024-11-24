from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.form.forms import AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.#


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/dashboard")
    return render(request, 'forms/auth/login.html')


def login_request(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("/dashboard")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("/dashboard")
        else:
            messages.error(request,"Invalid Credentials")
            return render(request, "authentication/login.html")
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

from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.login_user, name="home"),
    path('register', views.register_user, name="UserReg"),
    path('registration', views.register_request, name="registerUser"),
    path('login-user', views.login_request, name="loginUser"),
    path('logout', views.logout_view, name="logoutView"),
    path('forgot-password/', views.forgot_password_view, name="forgotPassword"),

]

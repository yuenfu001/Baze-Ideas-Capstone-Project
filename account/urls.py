from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user, name="home"),
    path('login-user', views.login_request, name="loginUser"),
    path('logout', views.logout_view, name="logoutView"),
    path('forgot-password/', views.forgot_password_view, name="forgotPassword"),

]

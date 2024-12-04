from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
# Create your form here.

class RegisterForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ["email","password1","password2"]


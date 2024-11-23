from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate
# Create your form here.

class RegisterForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ["phone_number","email", "password1","password2"]


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password')

    class Meta:
        model  =  Account
        fields =  ('email', 'password')

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class UserForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ["email", "first_name","last_name","phone_number","password1","password2"]
from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.core.exceptions import ValidationError

# Create your form here.



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ["first_name","email", "password","confirm_password","last_name","username"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Ensure passwords match
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user

# class RegisterForm(UserCreationForm):
# 	class Meta:
# 		model = Account
# 		fields = ["phone_number","email", "password1","password2"]


# class AccountAuthenticationForm(forms.ModelForm):
#     """
#       Form for Logging in  users
#     """
#     password  = forms.CharField(label= 'Password')
#
#     class Meta:
#         model  =  Account
#         fields =  ('email', 'password')
#
#     def clean(self):
#         if self.is_valid():
#
#             email = self.cleaned_data.get('email')
#             password = self.cleaned_data.get('password')
#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError('Invalid Login')
#
#
# class UserForm(UserCreationForm):
# 	class Meta:
# 		model = Account
# 		fields = ["email", "first_name","last_name","phone_number","password1","password2"]


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Authenticate the user using email instead of username
        user = authenticate(username=email, password=password)

        if user is None:
            raise forms.ValidationError("Invalid email or password")
        self.user_cache = user
        return self.cleaned_data







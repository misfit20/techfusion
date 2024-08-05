from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)


	class Meta:
		model = User
		fields = ["username", "email", "first_name","last_name", "password1", "password2"]

from django import forms
from django.forms import ModelForm
from emastersystem.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserProfileForm(ModelForm):
    class Meta:
        model=Employee
        exclude=('user',)
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'})
        }
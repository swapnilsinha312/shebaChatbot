from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,AbstractUser
from django import forms 

# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['name', 'email', 'password1', 'password2']

# class CreateUserForm(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
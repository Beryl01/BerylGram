from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Comment,Image

class Registration(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class postImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image','name','caption']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_pic','bio']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment',)






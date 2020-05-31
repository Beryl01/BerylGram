from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import Registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')
      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'auth/registration.html',{"form":form})
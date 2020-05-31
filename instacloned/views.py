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

@login_required
def index(request):
  comment_form = CommentForm()
  post_form = postImageForm()
  images = Image.display_images()
  users = User.objects.all()
  return render (request,'main/index.html',{"images":images,"comment_form":comment_form,"post":post_form,"all":users})

@login_required
def profile(request):
  current_user = request.user
  images = Image.objects.filter(user_id = current_user.id).all()
  return render(request,'auth/profile.html',{"images":images,"current_user":current_user})

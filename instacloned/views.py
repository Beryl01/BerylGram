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

@login_required
def post(request):
  if request.method == 'POST':
    post_form = postImageForm(request.POST,request.FILES) 
    if post_form.is_valid():
      the_post = post_form.save(commit = False)
      the_post.user = request.user
      the_post.save()
  return redirect('index')

@login_required
def commenting(request,image_id):
  c_form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    c_form = CommentForm(request.POST)
    if c_form.is_valid():
      comment = c_form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')
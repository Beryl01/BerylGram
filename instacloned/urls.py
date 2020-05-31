from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views as main_views

urlpatterns = [
    path('',main_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
    path('index/',main_views.index,name='index'),
    path('profile/',main_views.profile,name='profile'),
    path('post/',main_views.post,name='post'),
    re_path(r'^comment/(?P<image_id>\d+)$',main_views.commenting,name='commenting'),
    re_path(r'^allcomments/(?P<image_id>\d+)$',main_views.allcomments,name='allcomments'),
    re_path(r'^post_profile/(?P<pk>\d+)$',main_views.others_profile,name='others_profile'),
    re_path(r'^follow/(?P<user_id>\d+)$',main_views.follow,name='follow'),
    
 
]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )
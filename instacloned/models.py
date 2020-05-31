from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import datetime as dt
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
  image = models.ImageField(upload_to='images/' ,default='default.jpg')
  name = models.CharField(max_length=60)
  posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  caption = HTMLField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)

  def save_image(self):
     self.save()

  def delete_post(self):
    self.delete()   

  @classmethod
  def display_images(cls):
    images = cls.objects.all()
    return images

  @classmethod
  def search_images(cls,search_term):
    images = cls.objects.filter(name__icontains = search_term).all()
    return images  

  @property
  def all_comments(self):
    return self.comments.all()

  @property
  def all_likes(self):
    return self.imagelikes.count()

  class Meta:
        ordering = ['posted']  

  def __str__(self):
    return self.name

class Profile(models.Model):
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile/')
  bio = HTMLField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)

  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()

  def save_profile(self):
      self.save()

  def delete_profile(self):
      self.delete()  

  @property
  def all_followers(self):
    return self.followers.count()   

  @property
  def all_following(self):
    return self.following.count() 

  @property
  def follows(self):
    return [follow.followee for follow in self.following.all()]

  @property
  def following(self):
    return self.followers.all()

  @classmethod
  def search_profiles(cls,search_term):
    profiles = cls.objects.filter(user__username__icontains = search_term).all()
    return profiles

  def __str__(self):
    return self.bio  
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#Profile model
class Profile(models.Model): 
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  contact = models.CharField(max_length=10)
  country = models.CharField(max_length=50)
  location = models.CharField(max_length=255)
  latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
  longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
  important_areas = models.TextField()
  profile_pic = CloudinaryField('profile')
  
  def __str__(self):
    return self.user.username

#Riot model
class Riot(models.Model): 
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  location = models.CharField(max_length=30)
  date_posted = models.DateField(auto_now_add=True)
  time_riot_started = models.TimeField()
  riot_status = models.CharField(max_length=40) #ended or happening
  nature_of_riot = models.CharField(max_length=40) #peaceful or violent
  image = CloudinaryField('image')
  
  def __str__(self):
    return self.location
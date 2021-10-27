from django import forms
from .models import Profile
from django.contrib.auth.models import User

#User update form
class UserUpdateForm(forms.ModelForm): 
  class Meta: 
    model = User
    fields = ['username','email']
    
#Profile form
class ProfileUpdateForm(forms.ModelForm): 
  class Meta: 
    model = Profile
    fields = ['contact','country','location','important_areas','profile_pic']
from django.contrib import admin
from .models import Profile,Riot
from django.conf import settings

# Register your models here.
# admin.site.register(Profile)
admin.site.register(Riot)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
  list_display = ('user','contact','country','location','latitude','longitude','important_areas','profile_pic')
  search_fields = ('location',)
  
  fieldsets = (
    (None,{
      'fields':('user','contact','country','location','latitude','longitude','important_areas','profile_pic',)
    }),
  )
  class Media: 
    if hasattr(settings,'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY: 
      css = {
        'all':('css/styles.css',),
      }
      js = (
        'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
        'js/main.js',
      )
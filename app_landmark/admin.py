from django.contrib import admin

# Register your models here.
from app_landmark.models import Landmark

class MapAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    change_list_template = 'map.html'

admin.site.register(Landmark,MapAdmin)
from django.contrib import admin

# Register your models here.
from app_location.models import GeographyMockup, ProvinceMockup, AmphurMockup, DistrictMockup


class GeographyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name')
admin.site.register(GeographyMockup,GeographyAdmin)

class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','geo')
admin.site.register(ProvinceMockup,ProvinceAdmin)

class AmphurAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','province','geo')
admin.site.register(AmphurMockup,AmphurAdmin)

class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','amphur','province','geo')
admin.site.register(DistrictMockup,DistrictAdmin)
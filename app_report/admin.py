from django.contrib import admin

# Register your models here.
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter

from app_report.models import Products_Report, LogerReport, Profile_Report

admin.site.register(Profile_Report)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    search_fields = ['name','user__first_name','user__last_name']
    # autocomplete_fields = ['name',]
    list_display = ('name','user','price_type','price','price_start','price_end','enabled')
    list_filter = ('product_type','enabled','price_type','category')
    list_filter = (
        'product_type',
         'enabled',
        'price_type',
        'created_at',
        'status',
        ('category', ChoiceDropdownFilter),
    )
admin.site.register(Products_Report,ProductAdmin)

admin.site.register(LogerReport)
from django.contrib import admin

# Register your models here.
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter

from app_purchase.models import ProductMockup



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
    change_form_template = 'product.html'
    add_form_template = 'product.html'
admin.site.register(ProductMockup,ProductAdmin)
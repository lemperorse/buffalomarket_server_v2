from django.contrib import admin

# Register your models here.
from app_webconfig.models import ChoiceMockup, GroupFarmerMockup, CategoryMockup
from service_main.models import CategoryDetail


class Categoryline(admin.TabularInline):
    model = CategoryDetail
    fk_name = "category"
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

class CategoryAdmin(admin.ModelAdmin):
    inlines = [Categoryline, ]
    search_fields = ['name',]
    # autocomplete_fields = ['name',]
    list_display = ('name','enabled')
    list_filter = ('name','enabled')
admin.site.register(CategoryMockup,CategoryAdmin)

admin.site.register(ChoiceMockup)
admin.site.register(GroupFarmerMockup)


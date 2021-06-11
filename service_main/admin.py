from django.contrib import admin
from django.contrib.auth.models import User
from service_main.models.products import *
from service_main.models.profile import *
from service_main.models.general import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter, RelatedOnlyDropdownFilter



class ProfileAdmin(admin.ModelAdmin):
    # autocomplete_fields = [ 'province' ,'amphur' ,  'district'] #,
    list_filter = (
        ('local', DropdownFilter),
        ('geo', RelatedOnlyDropdownFilter),
        ('province', RelatedOnlyDropdownFilter),
        ('amphur', RelatedOnlyDropdownFilter),
        ('district', RelatedOnlyDropdownFilter),
    )
    search_fields = ['user__first_name','user__last_name', ]
    list_display = ('fullname','gender' ,'province', 'amphur', 'district','address','status' )
    change_list_template = 'reportUser.html'
    # change_form_template = 'reportUserForm.html'

    # class Media:. .
    #     js = ('multi_line_list_edit.js',)

admin.site.register(Profile,ProfileAdmin)

class UserProfileInline(admin.StackedInline):
    model = Profile
    autocomplete_fields = ['province', 'amphur', 'district']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name")
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','email',
                       'first_name', 'last_name'),
        }),
    )
    inlines = UserProfileInline,

admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)
admin.site.register(GroupsFarmer)


admin.site.register(ChoiceType)
admin.site.register(Choice)

# admin.site.register(Profile)
class FarmAdmin(admin.ModelAdmin):
    search_fields = ['name','user__first_name', 'user__last_name', ]
    list_display = ('name', 'owner', 'address', 'groupFull')
    autocomplete_fields = ['province', 'amphur', 'district']
    list_filter = (
        ('group', RelatedOnlyDropdownFilter),
        ('local', DropdownFilter),
        ('geo', RelatedOnlyDropdownFilter),
        ('province', RelatedOnlyDropdownFilter),
        ('amphur', RelatedOnlyDropdownFilter),
        ('district', RelatedOnlyDropdownFilter),
    )

admin.site.register(Farm,FarmAdmin)

class MapAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    change_list_template = 'reportMap.html'

admin.site.register(Map,MapAdmin)

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
admin.site.register(Category,CategoryAdmin)


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
admin.site.register(Product,ProductAdmin)

class GeographyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name')
admin.site.register(Geography,GeographyAdmin)

class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','geo')
admin.site.register(Province,ProvinceAdmin)

class AmphurAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','province','geo')
admin.site.register(Amphur,AmphurAdmin)

class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name','code']
    list_display = ('id','code', 'name','amphur','province','geo')
admin.site.register(District,DistrictAdmin)
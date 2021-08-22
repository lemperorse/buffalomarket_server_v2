from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter, RelatedOnlyDropdownFilter

from app_purchase.models import ProductMockup
from app_user.models import MyUser, Shop
from service_main.models import Profile, Farm


class FarmInline(admin.StackedInline):
    model = Farm


class UserProfileInline(admin.StackedInline):
    model = Profile
    # autocomplete_fields = ['province', 'amphur', 'district']


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
    list_display = ('username','first_name', 'last_name','address','is_superuser','is_staff','is_active')
    list_filter = (
        "is_superuser","is_staff","is_active","profile__local",
        
        ('profile__geo', RelatedOnlyDropdownFilter),
        ('profile__province', RelatedOnlyDropdownFilter),
        ('profile__amphur', RelatedOnlyDropdownFilter),
        ('profile__district', RelatedOnlyDropdownFilter),
    )
    inlines = UserProfileInline,
    change_form_template = 'user.html'
    add_form_template = 'user.html'

admin.site.register(MyUser,MyUserAdmin)



class ProductInline(admin.StackedInline):
    model = ProductMockup

class ShopAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user__first_name', 'user__last_name', ]
    list_display = ( 'name', 'owner', 'address', 'groupFull')
    list_filter = (
        ('group', RelatedOnlyDropdownFilter),
        "local",
        ('geo', RelatedOnlyDropdownFilter),
        ('province', RelatedOnlyDropdownFilter),
        ('amphur', RelatedOnlyDropdownFilter),
        ('district', RelatedOnlyDropdownFilter),
    )
    change_form_template = 'user.html'
    add_form_template = 'user.html'
    # inlines = ProductInline,
admin.site.register(Shop,ShopAdmin)
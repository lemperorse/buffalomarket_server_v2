from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import ugettext_lazy as _
from service_main.models.general import *
from location_field.models.plain import PlainLocationField
from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
)

GENDERS = (
    ('ชาย', 'ชาย'),
    ('หญิง', 'หญิง'),
)

LOCAL = (
    (True, 'ต่างประเทศ'),
    (False, 'ประเทศไทย'),
)

PREFIXES = (
    ('นาย', 'นาย'),
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว'),
)

class GroupsFarmer(models.Model):
    class Meta:
        verbose_name = _("กลุ่มเกษตรกร")
        verbose_name_plural = _("กลุ่มเกษตรกร")
    name = models.CharField(max_length=50, blank=True ,verbose_name="ชื่อกลุ่ม")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Profile(models.Model):
    class Meta:
        verbose_name = _("ข้อมูลผู้ใช้งานทั่วไป")
        verbose_name_plural = _("ข้อมูลผู้ใช้งานทั่วไป")
    user = models.OneToOneField(User, on_delete=models.CASCADE ,verbose_name="ผู้ใช้")
    prefix = models.CharField(max_length=255, choices=PREFIXES ,blank=True, null=True,verbose_name="คำนำหน้า")
    gender = models.CharField(max_length=255, choices=GENDERS ,blank=True, null=True,verbose_name="เพศ")
    personal_id = models.CharField(max_length=255, blank=True,verbose_name="เลขบัตรประจำตัวประชาชน")
    profile_image = models.ImageField(upload_to='Profile_image/', blank=True, null=True,verbose_name="รูปโปรไฟล์")
    presonal_image = models.ImageField(upload_to='Personal_image/', blank=True, null=True,verbose_name="สำเนาบัตรประจำตัวประชาชน")
    local = models.BooleanField(default=False,verbose_name="อาศัยอยู่ต่างประเทศ")
    my_address = models.CharField(max_length=500, blank=True,verbose_name="ที่อยู่")

    geo = models.ForeignKey(Geography, on_delete=models.CASCADE,verbose_name="ภูมิภาค",
        blank=True,
        null=True)
    province = ChainedForeignKey(
        "Province",
        chained_field="geo",
        chained_model_field="geo",
        show_all=False,
        auto_choose=True,
        verbose_name="จังหวัด",
        blank=True,
        null=True
    )

    amphur = ChainedForeignKey(
        "Amphur",
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        verbose_name="อำเภอ",
        blank=True,
        null=True
    )

    district = ChainedForeignKey(
        "District",
        chained_field="amphur",
        chained_model_field="amphur",
        show_all=False,
        auto_choose=True,
        verbose_name="ตำบล",
        blank=True,
        null=True
    )

    # province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="จังหวัด")
    # amphur = models.ForeignKey(Amphur, on_delete=models.CASCADE,verbose_name="อำเภอ")
    # district = models.ForeignKey(District, on_delete=models.CASCADE,verbose_name="ตำบล")
    zipcode = models.CharField(max_length=500, blank=True,verbose_name="รหัสไปรษณีย์")

    birthday = models.DateField(verbose_name="วันเกิด")
    age = models.FloatField(verbose_name="อายุ")
    status = models.BooleanField(default=True,verbose_name="สถานะการใช้งาน")
    email = models.CharField(max_length=500, blank=True,null=True,verbose_name="อีเมล์อื่นๆ")
    facebook = models.CharField(max_length=500, blank=True,null=True)
    line =  models.CharField(max_length=500, blank=True,null=True)
    tel = models.CharField(max_length=500, blank=True, null=True,verbose_name="เบอร์โทร")
    other = models.CharField(max_length=500, blank=True, null=True,verbose_name="การติดต่ออื่นๆ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user) + ">>>>" + str(self.created_at)
    @property
    def fullname(self):
        return self.user.first_name +" "+self.user.last_name
    @property
    def address(self):
        return self.province.name + "" + self.amphur.name + "" + self.district.name + "" + self.zipcode


class Farm(models.Model):
    class Meta:
        verbose_name = _("ข้อมูลฟาร์ม")
        verbose_name_plural = _("ข้อมูลฟาร์ม")
    name = models.CharField(max_length=50, blank=True, verbose_name="ชื่อฟาร์ม")
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name="เจ้าของฟาร์ม")
    group = models.ForeignKey(GroupsFarmer, on_delete=models.CASCADE, related_name='group',
                              blank=True, null=True,verbose_name="กลุ่มเกษตรกร")
    location = PlainLocationField(based_fields=['city'], zoom=7,default="19.8968 , 99.8309" ,verbose_name="แผนที่")
    local = models.BooleanField(default=False, verbose_name="อาศัยอยู่ต่างประเทศ")
    farm_address = models.CharField(max_length=500, null=True, blank=True, verbose_name='ที่อยู่',)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE, null=True, blank=True, verbose_name="ภูมิภาค")
    province = ChainedForeignKey(
        Province,
        chained_field="geo",
        chained_model_field="geo",
        show_all=False,
        auto_choose=True,
        null=True, blank=True,
        verbose_name="จังหวัด",
        sort=True)
    amphur = ChainedForeignKey(
        Amphur,
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        null=True, blank=True,
        verbose_name="อำเภอ",
        sort=True)
    district = ChainedForeignKey(
        District,
        chained_field="amphur",
        chained_model_field="amphur",
        show_all=False,
        auto_choose=True,
        null=True, blank=True,
        verbose_name="ตำบล",
        sort=True)

    zipcode = models.CharField(max_length=500, null=True, blank=True,  verbose_name="รหัสไปรษณีย์")
    farm_image = models.ImageField(upload_to='Farm_image/', null=True, blank=True,verbose_name="ภาพถ่ายฟาร์ม")
    email = models.CharField(max_length=500, blank=True, null=True ,verbose_name="อีเมล์ร้าน")
    facebook = models.CharField(max_length=500, blank=True, null=True )
    line = models.CharField(max_length=500, blank=True, null=True,verbose_name="ไลน์")
    tel = models.CharField(max_length=500, blank=True, null=True,verbose_name="เบอร์โทรฟาร์ม")
    other = models.CharField(max_length=500, blank=True, null=True,verbose_name="การติดต่ออื่นๆ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.name
        except:
            return "-"

        
    @property
    def address(self):
        try:
            return self.farm_address +""+ self.province.name + "" + self.amphur.name + "" + self.district.name + ""+ self.zipcode
        except:
            return self.farm_address

    address.fget.short_description = 'ที่อยู่ฟาร์ม'

    @property
    def owner(self):
        return self.user.first_name+" "+self.user.last_name
    owner.fget.short_description = 'เจ้าของฟาร์ม'

    @property
    def groupFull(self):
        try:
           return self.group.name
        except:
            return "-"
    groupFull.fget.short_description = 'กลุ่มเกษตรกร'

class Social(models.Model):
    pass
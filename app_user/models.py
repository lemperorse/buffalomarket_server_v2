from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from service_main.models import Farm


class MyUser(User):
    class Meta:
        proxy = True
        verbose_name = _("ข้อมูลผู้ใช้งานทั่วไป")
        verbose_name_plural = _("ข้อมูลผู้ใช้งานทั่วไป")
    def do_something(self):
        pass
    def __str__(self):
        return self.username

    @property
    def address(self):
        try:
            return self.profile.my_address  + "" + self.province.name + "" + self.amphur.name + "" + self.district.name + "" + self.zipcode
        except:
            return self.profile.my_address

    address.fget.short_description = 'ที่อยู่'

class Shop(Farm):
    class Meta:
        proxy = True
        verbose_name = _("ร้านค้า/ฟาร์ม")
        verbose_name_plural = _("ร้านค้า/ฟาร์ม")

    def __str__(self):
        return self.name

    @property
    def address(self):
        try:
            return self.farm_address + "" + self.province.name + "" + self.amphur.name + "" + self.district.name + "" + self.zipcode
        except:
            return self.farm_address

    address.fget.short_description = 'ที่อยู่ฟาร์ม'

    @property
    def owner(self):
        return self.user.first_name + " " + self.user.last_name

    owner.fget.short_description = 'เจ้าของฟาร์ม'

    @property
    def groupFull(self):
        try:
            return self.group.name
        except:
            return 'ไม่มีข้อมูล'


    groupFull.fget.short_description = 'กลุ่มเกษตรกร'

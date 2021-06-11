from django.db import models

# Create your models here.
from drf_api_logger.models import APILogsModel

from service_main.models import ChoiceType, GroupsFarmer, Category

from django.utils.translation import ugettext_lazy as _

class ChoiceMockup(ChoiceType):
    class Meta:
        proxy = True
        verbose_name = _("ตัวเลือก")
        verbose_name_plural = _("ตัวเลือก")
    def do_something(self):
        pass

class GroupFarmerMockup(GroupsFarmer):
    class Meta:
        proxy = True
        verbose_name = _("กลุ่มเกษตรกร")
        verbose_name_plural = _("กลุ่มเกษตรกร")
    def do_something(self):
        pass

class CategoryMockup(Category):
    class Meta:
        proxy = True
        verbose_name = _("สินค้า (ประเภท)")
        verbose_name_plural = _("สินค้า (ประเภท)")
    def do_something(self):
        pass

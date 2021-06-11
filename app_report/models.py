from django.db import models

# Create your models here.
from drf_api_logger.models import APILogsModel

from service_main.models import Product, Profile
from django.utils.translation import ugettext_lazy as _


class Profile_Report(Profile):
    class Meta:
        proxy = True
    def do_something(self):
        pass

class Products_Report(Product):
    class Meta:
        proxy = True
    def do_something(self):
        pass

class LogerReport(APILogsModel):
    class Meta:
        proxy = True
        verbose_name = _("รายงานความเคลื่อนไหว")
        verbose_name_plural = _("รายงานความเคลื่อนไหว")
    def do_something(self):
        pass
from django.db import models

# Create your models here.
from service_main.models import Product
from django.utils.translation import ugettext_lazy as _


class ProductMockup(Product):
    class Meta:
        proxy = True
        verbose_name = _("ประกาศ ซื้อ/ขาย")
        verbose_name_plural = _("ประกาศ ซื้อ/ขาย")
    def do_something(self):
        pass
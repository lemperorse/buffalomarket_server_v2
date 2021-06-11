from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from service_main.models import Map


class Landmark(Map):
    class Meta:
        proxy = True
        verbose_name = _("สถานที่สำคัญ")
        verbose_name_plural = _("สถานที่สำคัญ")
    def do_something(self):
        pass
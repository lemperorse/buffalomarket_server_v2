from django.db import models

# Create your models here.
from service_main.models import Geography, Province, Amphur, District
from django.utils.translation import ugettext_lazy as _


class GeographyMockup(Geography):
    class Meta:
        proxy = True
        verbose_name = _("ภูมิภาค")
        verbose_name_plural = _("ภูมิภาค")
    def do_something(self):
        pass
class ProvinceMockup(Province):
    class Meta:
        proxy = True
        verbose_name = _("จังหวัด")
        verbose_name_plural = _("จังหวัด")
    def do_something(self):
        pass
class AmphurMockup(Amphur):
    class Meta:
        proxy = True
        verbose_name = _("อำเภอ")
        verbose_name_plural = _("อำเภอ")
    def do_something(self):
        pass

class DistrictMockup(District):
    class Meta:
        proxy = True
        verbose_name = _("ตำบล")
        verbose_name_plural = _("ตำบล")
    def do_something(self):
        pass
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import ugettext_lazy as _

class Geography(models.Model):
    class Meta:
        verbose_name = _("(ที่อยู่) ภูมิภาค")
        verbose_name_plural = _("(ที่อยู่) ภูมิภาค")
    name = models.CharField(max_length=255)
    def __str__(self):
        return '{}'.format(self.name)


class Province(models.Model):
    class Meta:
        verbose_name = _("(ที่อยู่) จังหวัด")
        verbose_name_plural = _("(ที่อยู่) จังหวัด")
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=150)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)


class Amphur(models.Model):
    class Meta:
        verbose_name = _("(ที่อยู่) อำเภอ")
        verbose_name_plural = _("(ที่อยู่) อำเภอ")
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=150)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)


class District(models.Model):
    class Meta:
        verbose_name = _("(ที่อยู่) ตำบล")
        verbose_name_plural = _("(ที่อยู่) ตำบล")
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=150)
    amphur = models.ForeignKey(Amphur, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)


class ChoiceType(models.Model):
    class Meta:
        verbose_name = _("ประเภทตัวเลือก")
        verbose_name_plural = _("ประเภทตัวเลือก")
    name = models.CharField(max_length=255,verbose_name="ประเภทตัวเลือก")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.value

class Choice(models.Model):
    class Meta:
        verbose_name = _("ตัวเลือก")
        verbose_name_plural = _("ตัวเลือก")
    type = models.ForeignKey(ChoiceType,on_delete=models.CASCADE)
    value = models.CharField(max_length=255,verbose_name="ชื่อตัวเลือก")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.value


from django.db import models 
# Create your models here.
from polymorphic.models import PolymorphicModel
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import User
from django_pandas.managers import DataFrameManager

from service_main.models.profile import Farm
from location_field.models.plain import PlainLocationField

ProductType = [
        (0, 'ขาย'),
        (1, 'ซื้อ'),
    ]
SaleType = [
     (0, 'ชั่วคราว'),
     (1, 'ถาวร'),
]
PriceType = [
    (True, 'ราคาเต็ม'),
    (False, 'ช่วงราคา'),
]
#status: any = ['มีสินค้า', 'สินค้าหมด', 'ขายแล้ว', 'ยกเลิก'] ["รับซื้อ", "ได้รับสินค้าแล้ว", "ยกเลิก"],
productStatus = [
    (5, 'มีสินค้า'),
    (4, 'สินค้าหมด'),
    (3, 'ขายแล้ว'),
    (1, 'รับซื้อ'),
    (2, 'ได้รับสินค้าแล้ว'),
    (0, 'ยกเลิก'),
]
class Category(models.Model):
    class Meta:
        verbose_name = _("ประเภทสินค้า")
        verbose_name_plural = _("ประเภทสินค้า")
    name = models.CharField(max_length=255,verbose_name="ชื่อประเภทสินค้า")
    enabled = models.BooleanField(default=True,verbose_name="เปิดการใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class CategoryDetail(models.Model):
    class Meta:
        verbose_name = _("ข้อมูลในประเภทสินค้า")
        verbose_name_plural = _("ข้อมูลในประเภทสินค้า")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="ชื่อประเภทสินค้า")
    enabled = models.BooleanField(default=True,verbose_name="เปิดการใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Product(models.Model):
    class Meta:
        verbose_name = _("ประกาศ ซื้อ/ขาย")
        verbose_name_plural = _("ประกาศ ซื้อ/ขาย")
    name = models.CharField(max_length=255, verbose_name="ชื่อสินค้า")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="เจ้าของ")
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE,verbose_name="ร้านค้า",null=True, blank=True)
    category = models.ManyToManyField(CategoryDetail,verbose_name="ประเภทสินค้า")

    detail = models.TextField(null=True,blank=True,verbose_name="รายระเอียดสินค้า")
    product_type = models.IntegerField(default=0,null=True, blank=True, choices=ProductType, verbose_name="ประเภทสินค้า ซื้อ/ขาย")

    price_type = models.BooleanField(default=True,choices=PriceType,verbose_name="ประเภทราคา")
    price = models.FloatField(null=True,blank=True,verbose_name="ราคาสินค้า (ราคาเต็ม)")
    price_start = models.FloatField(null=True,blank=True,verbose_name="ช่วงราคาต่ำสุด (ช่วงราคา)")
    price_end = models.FloatField(null=True,blank=True,verbose_name="ช่วงราคาสูงสุด (ช่วงราคา)")

    file1 = models.FileField(upload_to='product/',null=True, blank=True,verbose_name="รูปสินค้า หรือวีดีโอ")
    file2 = models.FileField(upload_to='product/',null=True, blank=True,verbose_name="รูปสินค้า หรือวีดีโอ")
    file3 = models.FileField(upload_to='product/',null=True, blank=True,verbose_name="รูปสินค้า หรือวีดีโอ")
    file4 = models.FileField(upload_to='product/',null=True, blank=True,verbose_name="รูปสินค้า หรือวีดีโอ")
    file5 = models.FileField(upload_to='product/',null=True, blank=True,verbose_name="รูปสินค้า หรือวีดีโอ")
    sell_type =  models.IntegerField(null=True,blank=True,choices=SaleType ,verbose_name="ประเภทการขาย *ประกาศขาย")
    buy_date = models.DateField(null=True,blank=True,verbose_name="วันที่ปิดการขาย *ประกาศซื้อ")
    status =  models.IntegerField(null=True,blank=True,choices=productStatus,verbose_name="สถานะสินค้า")
    enabled = models.BooleanField(default=True,verbose_name="เปิดการใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Map(models.Model):
    class Meta:
        verbose_name = _("สถานที่สำคัญ")
        verbose_name_plural = _("สถานที่สำคัญ")
    name = models.CharField(max_length=255, verbose_name="ชื่อสถานที่สำคัญ")
    address = models.TextField( null=True, blank=True,verbose_name="ที่อยู่")
    location = PlainLocationField(based_fields=['city'], zoom=7, default="19.8968 , 99.8309", verbose_name="แผนที่")
    other = models.TextField(null=True, blank=True, verbose_name="อื่นๆ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
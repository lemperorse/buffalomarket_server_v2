# Generated by Django 3.2.4 on 2021-06-07 09:48

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_main', '0003_auto_20210607_0948'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
            ],
            options={
                'verbose_name': 'ข้อมูลผู้ใช้งานทั่วไป',
                'verbose_name_plural': 'ข้อมูลผู้ใช้งานทั่วไป',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
            ],
            options={
                'verbose_name': 'ร้านค้า/ฟาร์ม',
                'verbose_name_plural': 'ร้านค้า/ฟาร์ม',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service_main.farm',),
        ),
    ]

from django.contrib import admin
from django.conf.urls import url

# Register your models here.
from django.db import models

from service_core.views.admin.Report import index


class DummyModel(models.Model):
    class Meta:
        verbose_name = 'Link to my shiny custom view'
        app_label = 'service_core'  # or another app to put your custom view
class DummyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
                DummyModel._meta.app_label, DummyModel._meta.model_name)
        return [
            url(r'^my_view/$', index , name=view_name)
        ]

admin.site.register(DummyModel,DummyModelAdmin)
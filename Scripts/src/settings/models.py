from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Brand(models.Model):
    Brname=models.CharField(max_length=50 , verbose_name="Name")
    Brdesc=models.TextField(blank=True,null=True , verbose_name="Description")
    

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.Brname

class Variant(models.Model):
    Varname=models.CharField(max_length=50 , verbose_name="Name")
    Vardesc=models.TextField(blank=True,null=True , verbose_name="Description")

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.Varname


# from distutils.command.upload import upload
# from unicodedata import category, name
from distutils.command.upload import upload

from django.db import models

from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify

from django.urls import reverse

# Create your models here.

# def image_upload(instance,filename):
#     imagename,extension = filename.split(".")
#     return "jobs/%s.%s"%(instance.id,extension)

class Product(models.Model):
    proName=models.CharField(max_length=100 , verbose_name=_("Product Name"))
    proCategory=models.ForeignKey('Category', on_delete=models.CASCADE ,blank=True , null=True , verbose_name=_(" category"))
    probrand=models.ForeignKey('settings.Brand', on_delete=models.CASCADE , blank=True , null=True , verbose_name=_(" brand"))
    proDesc=models.TextField(verbose_name=_(" Description"))
    proImg=models.ImageField(upload_to='media/product/', blank=True , null=True,verbose_name=_(" Iamge"))
    proPrice=models.DecimalField(max_digits=10 ,decimal_places=2 ,verbose_name=_(" Price"))
    proDiscount=models.DecimalField(max_digits=6 ,decimal_places=2 ,verbose_name=_(" Discount"))
    # proDiscountPrice=models.DecimalField(max_digits=10 ,decimal_places=2 ,verbose_name=_(" Discount"))
    proCost=models.DecimalField(max_digits=10 ,decimal_places=2 , verbose_name=_(" Cost"))
    proCreated=models.DateTimeField(verbose_name=_(" Created at"))
    proslug=models.SlugField(blank=True,null=True,verbose_name=_(" slug"))
    
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.proslug})
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    
    def save(self,*args,**kwargs):
        if not self.proslug :
            self.proslug = slugify(self.proName)
            super(Product,self).save(*args, **kwargs)
    
    
    def __str__(self) :
        return self.proName
    

class ProductImg(models.Model):
    proName = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=_("product"))
    proImage = models.ImageField(upload_to="ProductImg/",verbose_name=("Image"))
    
    def __str__(self):
        return str(self.proName)
    
class Category(models.Model):
    CatMain=models.CharField(max_length=50 ,verbose_name=_("Name"))
    CatParent= models.ForeignKey('self',limit_choices_to={'CatParent__isnull' : True},on_delete=models.CASCADE ,blank=True, null=True,verbose_name=_("Main_category"))
    CatDesc=models.TextField(verbose_name=_("Description"))
    CatImg=models.ImageField(upload_to='category/',verbose_name=_("Image"))
    
    def __str__(self):
        return self.CatMain
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Product_Alternative(models.Model):
    PALproduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_("product"))
    PALalternative=models.ManyToManyField(Product,related_name='Alternative_products',verbose_name=_("Alternative"))

    class Meta:
        verbose_name = _("Product_Alternative")
        verbose_name_plural = _("Product_Alternatives")

    def __str__(self):
        return str(self.PALproduct)


class Product_Accessories(models.Model):
    PACCproduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainACC_product',verbose_name=_("product"))
    PACCalternative=models.ManyToManyField(Product,related_name='Accessories_products',verbose_name=_("Accessories"))
    

    class Meta:
        verbose_name = _("Product_Accessory")
        verbose_name_plural = _("Product_Accessories")

    def __str__(self):
        return str(self.PACCproduct)

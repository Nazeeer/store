from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name=_("user"))
    country=CountryField()
    image=models.ImageField(upload_to='profile',blank=True,null=True,verbose_name=_("image"))
    addres=models.CharField(max_length=50,verbose_name=_("address"))
    join_date=models.DateTimeField(verbose_name=_("created at"),default= datetime.datetime.now)
    slug=models.SlugField(blank=True,null=True,verbose_name=_("slug"))

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.user.username)
            super(Profile,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})

# def createProfile(sender,*args, **kwargs):
#     if kwargs['created']:
#         user_profile= Profile.objects.create(user=kwargs['instance'])
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
    
# post_save.connect(createProfile,sender=User)

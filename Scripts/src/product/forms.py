from dataclasses import fields
from pyexpat import model
from django import forms


from .models import Product

class ApplyForm(forms.ModelForm):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model= Product 
        fields='__all__'

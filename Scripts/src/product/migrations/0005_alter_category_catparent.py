# Generated by Django 4.1 on 2022-08-22 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CatParent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]

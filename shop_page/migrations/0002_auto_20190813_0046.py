# Generated by Django 2.2.1 on 2019-08-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to='image/', verbose_name='image'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_page', '0004_auto_20190817_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_page', '0002_goods_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='title3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

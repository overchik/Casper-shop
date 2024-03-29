# Generated by Django 2.2.1 on 2019-08-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_page', '0003_goods_title3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='title3',
        ),
        migrations.AddField(
            model_name='goods',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]

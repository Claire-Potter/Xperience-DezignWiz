# Generated by Django 3.2.9 on 2021-12-19 22:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0017_auto_20211219_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='survey_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='efeeyko4svga74cweezl', max_length=255, null=True, verbose_name='image'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0026_auto_20211119_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='videotwo_name',
            field=models.CharField(default='placeholder', max_length=80),
        ),
    ]

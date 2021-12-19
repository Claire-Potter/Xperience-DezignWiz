# Generated by Django 3.2.9 on 2021-12-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0055_auto_20211219_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='do_not_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='images',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='progress',
            name='do_not_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='step',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
    ]
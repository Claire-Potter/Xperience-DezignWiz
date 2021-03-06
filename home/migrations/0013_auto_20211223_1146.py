# Generated by Django 3.2.9 on 2021-12-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211219_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='home',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='verification',
            name='do_not_delete',
        ),
        migrations.AddField(
            model_name='contact',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='home',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='verification',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-10 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={},
        ),
        migrations.RemoveField(
            model_name='home',
            name='order_number',
        ),
    ]

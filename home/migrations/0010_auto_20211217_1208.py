# Generated by Django 3.2.9 on 2021-12-17 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211217_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Contact_Requests'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Home'},
        ),
        migrations.AlterModelOptions(
            name='verification',
            options={'get_latest_by': ['updated_on'], 'ordering': ['updated_on'], 'verbose_name_plural': 'Verification_Id'},
        ),
    ]

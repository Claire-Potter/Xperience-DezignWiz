# Generated by Django 3.2.9 on 2021-12-10 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0043_alter_progress_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0029_auto_20211122_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='slug_template',
            field=models.SlugField(default='steps_document', max_length=80),
        ),
    ]
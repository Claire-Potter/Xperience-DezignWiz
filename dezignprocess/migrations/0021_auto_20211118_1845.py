# Generated by Django 3.2.9 on 2021-11-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0020_step_step_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='step',
            name='link',
            field=models.URLField(default='https://8000-plum-cat-mt2ogx7v.ws-eu18.gitpod.io/'),
        ),
    ]
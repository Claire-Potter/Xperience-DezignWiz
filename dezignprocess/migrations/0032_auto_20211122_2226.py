# Generated by Django 3.2.9 on 2021-11-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0031_rename_slug_template_template_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='step',
            field=models.ManyToManyField(to='dezignprocess.Step'),
        ),
        migrations.RemoveField(
            model_name='step',
            name='templates',
        ),
        migrations.AddField(
            model_name='step',
            name='templates',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
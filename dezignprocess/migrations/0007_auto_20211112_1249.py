# Generated by Django 3.2.9 on 2021-11-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0006_auto_20211111_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepTwo',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dezignprocess.step',),
        ),
        migrations.AddField(
            model_name='step',
            name='list_number',
            field=models.IntegerField(default=1),
        ),
    ]

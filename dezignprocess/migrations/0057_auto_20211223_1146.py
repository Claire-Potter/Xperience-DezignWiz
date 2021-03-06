# Generated by Django 3.2.9 on 2021-12-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0056_auto_20211219_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='images',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='step',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='do_not_delete',
        ),
        migrations.AddField(
            model_name='comment',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='images',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='progress',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='step',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='tool',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='step',
            name='list_number',
            field=models.IntegerField(default='0', editable=False),
        ),
        migrations.AlterField(
            model_name='step',
            name='order_number',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='step',
            name='slug',
            field=models.SlugField(editable=False, max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='title',
            field=models.CharField(editable=False, max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='order_number',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='tool',
            name='slug',
            field=models.SlugField(default='steps_document', editable=False, max_length=80),
        ),
        migrations.AlterField(
            model_name='tool',
            name='title',
            field=models.CharField(default='placeholder', editable=False, max_length=80, unique=True),
        ),
    ]

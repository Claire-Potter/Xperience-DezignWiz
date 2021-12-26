# Generated by Django 3.2.9 on 2021-12-23 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0059_auto_20211223_1154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'get_latest_by': ['added'], 'ordering': ['order_number']},
        ),
        migrations.AlterField(
            model_name='progress',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='step',
            name='feature_image',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='featured_image', to='dezignprocess.image'),
        ),
    ]
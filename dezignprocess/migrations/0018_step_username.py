# Generated by Django 3.2.9 on 2021-11-16 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dezignprocess', '0017_remove_comment_dezign_thinker'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='username',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE,
            related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]

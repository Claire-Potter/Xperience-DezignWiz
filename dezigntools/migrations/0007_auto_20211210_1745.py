# Generated by Django 3.2.9 on 2021-12-10 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0006_remove_survey_include_default_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='text',
            new_name='option',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='prompt',
            new_name='question',
        ),
    ]

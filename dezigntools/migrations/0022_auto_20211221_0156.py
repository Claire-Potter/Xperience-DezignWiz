# Generated by Django 3.2.9 on 2021-12-21 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0021_agequestion_genderquestion_industryquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='agerange',
            name='age_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dezigntools.agequestion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gender',
            name='gender_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dezigntools.genderquestion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industry',
            name='industry_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dezigntools.agequestion'),
            preserve_default=False,
        ),
    ]

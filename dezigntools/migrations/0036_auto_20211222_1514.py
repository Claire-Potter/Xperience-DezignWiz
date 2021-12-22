# Generated by Django 3.2.9 on 2021-12-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0035_defaultanswers_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agequestion',
            name='age_question',
            field=models.CharField(default='Please select your age range:', editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='agerange',
            name='order_number',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='agerange',
            name='title',
            field=models.CharField(editable=False, max_length=80),
        ),
        migrations.AlterField(
            model_name='gender',
            name='order_number',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(editable=False, max_length=80),
        ),
        migrations.AlterField(
            model_name='genderquestion',
            name='gender_question',
            field=models.CharField(default='Please select your preferred gender:', editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='industry',
            name='title',
            field=models.CharField(editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='industryquestion',
            name='industry_question',
            field=models.CharField(default='Please select your Industry of employment:', editable=False, max_length=128),
        ),
    ]

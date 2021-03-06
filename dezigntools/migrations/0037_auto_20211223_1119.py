# Generated by Django 3.2.9 on 2021-12-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0036_auto_20211222_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agequestion',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='agerange',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='defaultoptions',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='genderquestion',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='industryquestion',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='option',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='question',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='do_not_delete',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='do_not_delete',
        ),
        migrations.AddField(
            model_name='agequestion',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='agerange',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='defaultanswers',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='defaultoptions',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='gender',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='genderquestion',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='industry',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='industryquestion',
            name='deletable',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='option',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='question',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='deletable',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='agequestion',
            name='age_question',
            field=models.CharField(default='Please select your age range:', max_length=128),
        ),
        migrations.AlterField(
            model_name='agerange',
            name='order_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agerange',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='gender',
            name='order_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='genderquestion',
            name='gender_question',
            field=models.CharField(default='Please select your preferred gender:', max_length=128),
        ),
        migrations.AlterField(
            model_name='industry',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='industryquestion',
            name='industry_question',
            field=models.CharField(default='Please select your Industry of employment:', max_length=128),
        ),
    ]

# Generated by Django 4.1 on 2022-08-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emastersystem', '0004_rename_experience_employee_yearofexperience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='companyname',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
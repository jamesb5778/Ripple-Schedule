# Generated by Django 3.2.9 on 2021-11-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpNumber',
            field=models.IntegerField(),
        ),
    ]
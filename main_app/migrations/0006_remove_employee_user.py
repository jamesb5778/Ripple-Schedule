# Generated by Django 3.2.9 on 2021-11-20 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]

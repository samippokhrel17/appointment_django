# Generated by Django 4.2.5 on 2023-10-13 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0005_remove_appoinment_appoinment_cancel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='appoinment_id',
        ),
    ]

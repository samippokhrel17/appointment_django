# Generated by Django 4.2.5 on 2023-10-13 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoinment',
            name='appoinment_cancel',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='appoinment_complete',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='time',
        ),
        migrations.AddField(
            model_name='appoinment',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]

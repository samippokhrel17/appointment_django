# Generated by Django 4.2.5 on 2023-10-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainbranch',
            name='branch_id',
        ),
        migrations.AddField(
            model_name='mainbranch',
            name='branch_id',
            field=models.ManyToManyField(to='appoint.branch'),
        ),
    ]

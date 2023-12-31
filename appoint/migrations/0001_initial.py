# Generated by Django 4.2.5 on 2023-10-08 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('appoinment_cancel', models.BooleanField(default=False)),
                ('appoinment_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('appoinment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appoint.appoinment')),
            ],
        ),
        migrations.CreateModel(
            name='Mainbranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appoint.branch')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-20 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('profession', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('connected_year', models.IntegerField()),
                ('connected_source', models.CharField(max_length=100)),
                ('working_place', models.CharField(max_length=255)),
                ('native_place', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info_contacts', to='business_info.business')),
            ],
        ),
    ]

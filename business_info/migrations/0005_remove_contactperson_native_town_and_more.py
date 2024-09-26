# Generated by Django 5.1.1 on 2024-09-22 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_info', '0004_alter_contactperson_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactperson',
            name='native_town',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='whatsapp_number',
        ),
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='level',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='name_of_firm',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='website_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactperson_set', to='business_info.business'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='description',
            field=models.TextField(default='N/A', verbose_name='Описание'),
        ),
    ]

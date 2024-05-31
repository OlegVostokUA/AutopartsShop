# Generated by Django 5.0.6 on 2024-05-30 19:33

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_component_currency'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
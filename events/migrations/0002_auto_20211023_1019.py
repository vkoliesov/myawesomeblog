# Generated by Django 3.2.8 on 2021-10-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_text',
            new_name='text',
        ),
    ]

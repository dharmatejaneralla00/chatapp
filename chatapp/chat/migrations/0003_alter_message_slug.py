# Generated by Django 4.2.7 on 2023-11-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_roomid_slug_message_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='slug',
            field=models.SlugField(),
        ),
    ]

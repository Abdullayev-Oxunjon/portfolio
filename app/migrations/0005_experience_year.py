# Generated by Django 4.2.1 on 2023-08-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_about_social_network_about_social_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

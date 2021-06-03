# Generated by Django 3.1.8 on 2021-06-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0003_remove_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlangroup',
            name='max_vid',
            field=models.PositiveIntegerField(default=4094),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='min_vid',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

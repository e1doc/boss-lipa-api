
# Generated by Django 3.0.8 on 2022-04-24 13:21
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_auto_20211125_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspermitapplication',
            name='is_renewal',
            field=models.BooleanField(default=False),
        ),
    ]

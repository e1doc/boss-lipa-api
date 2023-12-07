# Generated by Django 3.0.8 on 2020-12-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201203_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessactivity',
            name='application_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='businessactivity',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

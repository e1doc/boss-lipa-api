# Generated by Django 3.0.8 on 2021-01-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20210114_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetails',
            name='president_first_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='president_last_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='president_middle_name',
            field=models.TextField(blank=True),
        ),
    ]
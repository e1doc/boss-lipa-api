# Generated by Django 3.0.8 on 2021-11-25 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_auto_20211125_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildingapplicationrequirements',
            options={'ordering': ('-updated_at',)},
        ),
    ]
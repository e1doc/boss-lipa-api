# Generated by Django 3.0.8 on 2021-03-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_buildingpermitapplication_inspection_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landbanktransaction',
            name='payment_option',
            field=models.TextField(blank=True, null=True),
        ),
    ]
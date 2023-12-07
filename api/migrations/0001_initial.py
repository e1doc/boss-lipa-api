# Generated by Django 3.0.8 on 2020-11-21 14:43

import api.custom_storage
import api.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_year', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('batch', models.CharField(blank=True, max_length=20)),
                ('appointment_date', models.DateTimeField(blank=True, null=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentLimit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('batch', models.CharField(blank=True, max_length=50)),
                ('count', models.IntegerField(blank=True, default=0)),
                ('remaining', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference_number', models.CharField(blank=True, max_length=50)),
                ('quarter', models.CharField(blank=True, max_length=20)),
                ('amount', models.FloatField(blank=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillFees',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=50)),
                ('fee_description', models.CharField(blank=True, max_length=50)),
                ('amount', models.FloatField(blank=True)),
                ('penalty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingApplicationRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_year', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingBasicInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(blank=True, max_length=20)),
                ('owner_first_name', models.CharField(blank=True, max_length=50)),
                ('owner_middle_name', models.CharField(blank=True, max_length=50)),
                ('owner_last_name', models.CharField(blank=True, max_length=50)),
                ('owner_complete_address', models.CharField(blank=True, max_length=50)),
                ('owner_zip_code', models.CharField(blank=True, max_length=50)),
                ('owner_telephone_number', models.CharField(blank=True, max_length=50)),
                ('ownership_type', models.CharField(blank=True, max_length=50)),
                ('tin', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingDeptAssessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_no', models.CharField(blank=True, max_length=50)),
                ('form_of_ownership', models.CharField(blank=True, max_length=50)),
                ('lot_no', models.CharField(blank=True, max_length=20)),
                ('blk_no', models.CharField(blank=True, max_length=20)),
                ('tct_no', models.CharField(blank=True, max_length=20)),
                ('tax_dec_no', models.CharField(blank=True, max_length=20)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('barangay', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('scope_of_work', models.CharField(blank=True, max_length=50)),
                ('scope_of_work_others', models.CharField(blank=True, max_length=50)),
                ('character_of_occupancy', models.CharField(blank=True, max_length=50)),
                ('character_of_occupancy_others', models.CharField(blank=True, max_length=50)),
                ('property_type', models.CharField(blank=True, max_length=20)),
                ('address_no', models.CharField(blank=True, max_length=20)),
                ('lot_no_count', models.CharField(blank=True, max_length=20)),
                ('phase_no', models.CharField(blank=True, max_length=20)),
                ('subdivision_name', models.CharField(blank=True, max_length=20)),
                ('district', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingEvaluationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(null=True, storage=api.custom_storage.PrivateMediaStorage(), upload_to=api.models.MessageAttachment.get_user_image_folder)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingOtherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupancy_classified', models.CharField(blank=True, max_length=50)),
                ('total_estimated_cost', models.FloatField(blank=True)),
                ('units', models.IntegerField()),
                ('floor_area', models.IntegerField()),
                ('lot_area', models.IntegerField()),
                ('date_of_construction', models.DateTimeField(blank=True, null=True)),
                ('date_of_completion', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingPermitApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_draft', models.BooleanField(blank=True, default=True)),
                ('application_status', models.IntegerField(default=0)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_disapprove', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('date_renewed', models.DateTimeField(blank=True, null=True)),
                ('is_enrolled', models.BooleanField(default=False)),
                ('last_submitted', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingRequirementFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=100)),
                ('requirements_label', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(null=True, storage=api.custom_storage.PrivateMediaStorage(), upload_to=api.models.BuildingRequirementFiles.get_user_image_folder)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingRequirementsChecklist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50)),
                ('line_of_business', models.CharField(blank=True, max_length=50)),
                ('capitalization', models.CharField(blank=True, max_length=50)),
                ('essential', models.CharField(blank=True, max_length=50)),
                ('units', models.IntegerField(blank=True, default=0, null=True)),
                ('non_essential', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessBasicInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dti_sec_cda_reg_number', models.CharField(blank=True, default='', max_length=50)),
                ('dti_sec_cda_reg_date', models.DateTimeField(blank=True, null=True)),
                ('type_of_organization', models.CharField(blank=True, max_length=20)),
                ('ctc_no', models.CharField(blank=True, max_length=20)),
                ('tin', models.CharField(blank=True, max_length=20)),
                ('has_tax_incentive', models.BooleanField(blank=True, default=False)),
                ('government_entity', models.CharField(blank=True, max_length=50)),
                ('reference_number', models.CharField(blank=True, max_length=20)),
                ('owner_first_name', models.CharField(blank=True, max_length=50)),
                ('owner_middle_name', models.CharField(blank=True, max_length=50)),
                ('owner_last_name', models.CharField(blank=True, max_length=50)),
                ('owner_complete_address', models.CharField(blank=True, max_length=100)),
                ('owner_email_address', models.CharField(blank=True, max_length=50)),
                ('owner_telephone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('owner_mobile_number', models.CharField(blank=True, max_length=50)),
                ('mode_of_payment', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessDeptAssessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('trade_name', models.CharField(blank=True, max_length=50)),
                ('complete_business_address', models.CharField(blank=True, max_length=100)),
                ('president_first_name', models.CharField(blank=True, max_length=50)),
                ('president_middle_name', models.CharField(blank=True, max_length=50)),
                ('president_last_name', models.CharField(blank=True, max_length=50)),
                ('telephone_number', models.CharField(blank=True, max_length=50)),
                ('email_address', models.CharField(blank=True, max_length=50)),
                ('property_index_number', models.CharField(blank=True, max_length=50)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('total_employees', models.IntegerField(blank=True, null=True)),
                ('residing_employees', models.IntegerField(blank=True, null=True)),
                ('address_no', models.CharField(blank=True, max_length=50)),
                ('subdivision', models.CharField(blank=True, max_length=50)),
                ('unit_no', models.CharField(blank=True, max_length=50)),
                ('floor_no', models.CharField(blank=True, max_length=50)),
                ('house_no', models.CharField(blank=True, max_length=50)),
                ('block_no', models.CharField(blank=True, max_length=50)),
                ('lot_no', models.CharField(blank=True, max_length=50)),
                ('building_no', models.CharField(blank=True, max_length=50)),
                ('building_name', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('barangay', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPermitApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=50)),
                ('application_status', models.IntegerField(default=0)),
                ('is_draft', models.BooleanField(blank=True, default=True)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_disapprove', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('date_renewed', models.DateTimeField(blank=True, null=True)),
                ('is_enrolled', models.BooleanField(default=False)),
                ('last_submitted', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('application_type', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('index', models.IntegerField(default=0)),
                ('business_index', models.IntegerField(default=0)),
                ('building_index', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('complete_address', models.CharField(blank=True, max_length=100)),
                ('telephone_number', models.CharField(blank=True, max_length=50)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None)),
                ('email_address', models.CharField(blank=True, max_length=50)),
                ('gross_monthly_rental', models.FloatField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequirementFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=100)),
                ('requirements_label', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(null=True, storage=api.custom_storage.PrivateMediaStorage(), upload_to=api.models.RequirementFiles.get_user_image_folder)),
            ],
        ),
        migrations.CreateModel(
            name='Soa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date_issued', models.DateTimeField(null=True)),
                ('year', models.CharField(blank=True, max_length=20)),
                ('quarter', models.CharField(blank=True, max_length=20)),
                ('paymode', models.CharField(blank=True, max_length=20)),
                ('amount', models.FloatField(blank=True)),
                ('application_type', models.CharField(blank=True, max_length=50)),
                ('reference_number', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_remarks', models.BooleanField(blank=True, default=False)),
                ('subject', models.TextField()),
                ('status', models.CharField(blank=True, default='pending', max_length=50)),
                ('is_responded', models.BooleanField(blank=True, default=False)),
                ('is_resolved', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('building_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildingremarks', to='api.BuildingPermitApplication')),
                ('business_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businessremarks', to='api.BusinessPermitApplication')),
            ],
        ),
    ]

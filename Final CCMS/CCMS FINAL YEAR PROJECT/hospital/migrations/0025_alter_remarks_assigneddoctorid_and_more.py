# Generated by Django 4.2.6 on 2024-04-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0024_alter_remarks_assigneddoctorid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remarks",
            name="assignedDoctorId",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="remarks",
            name="patientId",
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2024-04-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0022_patient_remarks_delete_remarks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Remarks",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assignedDoctorId", models.IntegerField()),
                ("patientId", models.IntegerField()),
                ("remarks", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="patient",
            name="remarks",
        ),
    ]

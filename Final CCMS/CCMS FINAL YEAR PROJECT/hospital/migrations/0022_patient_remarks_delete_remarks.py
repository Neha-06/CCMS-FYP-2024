# Generated by Django 4.2.6 on 2024-04-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0021_remarks"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="remarks",
        ),
    ]
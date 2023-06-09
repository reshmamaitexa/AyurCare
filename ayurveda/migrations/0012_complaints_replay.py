# Generated by Django 4.1.5 on 2023-04-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ayurveda", "0011_complaints"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complaints_Replay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient", models.CharField(max_length=50)),
                ("complaint", models.CharField(max_length=500)),
                ("date", models.DateField()),
                ("replay", models.CharField(max_length=500)),
                ("complaint_status", models.CharField(max_length=10)),
            ],
        ),
    ]

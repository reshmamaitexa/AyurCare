# Generated by Django 4.1.5 on 2023-04-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ayurveda", "0007_packages"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
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
                ("medicine_name", models.CharField(max_length=50)),
                ("medicine_qnty", models.CharField(max_length=50)),
                ("medicine_description", models.CharField(max_length=500)),
                ("medicine_dosage", models.CharField(max_length=500)),
                ("medicine_usage", models.CharField(max_length=500)),
                ("medicine_price", models.CharField(max_length=50)),
                ("medicine_photo", models.ImageField(upload_to="images")),
                ("medicine_status", models.CharField(max_length=10)),
            ],
        ),
    ]

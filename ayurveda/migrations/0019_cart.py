# Generated by Django 4.1.5 on 2023-05-30 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ayurveda", "0018_package_books_treatments_package_payment_tb"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("medicine_name", models.CharField(max_length=500)),
                ("medicine_qnty", models.CharField(max_length=500)),
                ("medicine_price", models.CharField(max_length=500)),
                ("cart_status", models.CharField(max_length=10)),
                ("medicine_photo", models.ImageField(upload_to="images")),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ayurveda.medicine",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ayurveda.patient",
                    ),
                ),
            ],
        ),
    ]
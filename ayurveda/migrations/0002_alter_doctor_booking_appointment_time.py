# Generated by Django 4.1.5 on 2023-04-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ayurveda", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor_booking",
            name="appointment_time",
            field=models.CharField(max_length=40),
        ),
    ]

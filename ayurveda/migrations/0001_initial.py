# Generated by Django 4.1.5 on 2023-04-10 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("doctorname", models.CharField(max_length=20)),
                ("doctorqualification", models.CharField(max_length=20)),
                ("doctorexperience", models.CharField(max_length=20)),
                ("doctoremail", models.EmailField(max_length=20)),
                ("doctorphone", models.CharField(max_length=20)),
                ("doctorspecialization", models.CharField(max_length=50)),
                ("doctorgender", models.CharField(max_length=20)),
                ("doctor_available_days", models.CharField(max_length=40)),
                ("doctor_available_time", models.CharField(max_length=40)),
                ("doctorprofile_photo", models.ImageField(upload_to="images")),
                ("role", models.CharField(max_length=10)),
                ("doctorstatus", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Log",
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
                ("username", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=20, unique=True)),
                ("role", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("patientname", models.CharField(max_length=20)),
                ("patientage", models.CharField(max_length=20)),
                ("patientgender", models.CharField(max_length=20)),
                ("patientemail", models.EmailField(max_length=20)),
                ("patientphone", models.CharField(max_length=20)),
                ("patientaddress", models.CharField(max_length=50)),
                ("patientplace", models.CharField(max_length=20)),
                ("patientpost", models.CharField(max_length=20)),
                ("patientpincode", models.CharField(max_length=20)),
                ("role", models.CharField(max_length=10)),
                ("patientstatus", models.CharField(max_length=10)),
                (
                    "log_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="ayurveda.log"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor_Booking",
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
                ("appointment_date", models.DateField()),
                ("appointment_time", models.DateField()),
                ("bookingstatus", models.CharField(max_length=10)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ayurveda.doctor",
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
        migrations.AddField(
            model_name="doctor",
            name="log_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="ayurveda.log"
            ),
        ),
    ]

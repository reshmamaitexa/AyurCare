# Generated by Django 4.1.5 on 2023-04-29 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ayurveda", "0009_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="review_photo",
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_studentfeedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentfeedback",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]

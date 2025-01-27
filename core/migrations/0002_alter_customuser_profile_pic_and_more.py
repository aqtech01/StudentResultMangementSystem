# Generated by Django 5.0.6 on 2024-07-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(upload_to="profile_pic"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "HOD"), (2, "Staff"), (3, "Student")], default=1
            ),
        ),
    ]

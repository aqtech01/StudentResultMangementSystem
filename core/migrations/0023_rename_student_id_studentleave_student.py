# Generated by Django 5.0.7 on 2024-07-26 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_rename_student_studentleave_student_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentleave",
            old_name="student_id",
            new_name="student",
        ),
    ]

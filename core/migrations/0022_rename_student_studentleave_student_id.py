# Generated by Django 5.0.7 on 2024-07-26 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_rename_student_id_studentleave_student"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentleave",
            old_name="student",
            new_name="student_id",
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_journal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="journalmodel",
            name="category",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-14 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="created_at",
        ),
    ]

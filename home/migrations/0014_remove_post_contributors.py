# Generated by Django 5.0.2 on 2024-02-11 06:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_remove_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="contributors",
        ),
    ]

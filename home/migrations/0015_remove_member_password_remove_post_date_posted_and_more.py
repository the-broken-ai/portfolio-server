# Generated by Django 5.0.2 on 2024-02-11 07:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_remove_post_contributors"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="password",
        ),
        migrations.RemoveField(
            model_name="post",
            name="date_posted",
        ),
        migrations.RemoveField(
            model_name="post",
            name="repository",
        ),
        migrations.AddField(
            model_name="member",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="home.member",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="github",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="member",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="posts/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
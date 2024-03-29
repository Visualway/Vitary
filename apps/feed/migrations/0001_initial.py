# Generated by Django 4.2.7 on 2023-11-22 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Plustag",
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
                ("name", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("rating", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ["-rating"],
            },
        ),
        migrations.CreateModel(
            name="Feed",
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
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("like_count", models.IntegerField(default=0)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="You can upload upto one image per feed",
                        null=True,
                        upload_to="uploads/images/",
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        help_text="You can upload upto one video per feed",
                        null=True,
                        upload_to="uploads/videos/",
                    ),
                ),
                (
                    "nsfw",
                    models.BooleanField(
                        default=False,
                        help_text="Mark as NSFW if the content is not safe for work",
                        verbose_name="Is the Content NSFW?",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_feeds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "mentions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="mentioned_feeds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("plustag", models.ManyToManyField(blank=True, to="feed.plustag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feeds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "feed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="feed.feed"
                    ),
                ),
                (
                    "reply_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="feed.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]

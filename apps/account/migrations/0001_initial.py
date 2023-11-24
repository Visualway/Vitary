# Generated by Django 4.2.7 on 2023-11-22 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("follower_count", models.IntegerField(default=0, editable=False)),
                ("following_count", models.IntegerField(default=0, editable=False)),
                (
                    "email_notif",
                    models.BooleanField(
                        default=True, verbose_name="Get Email Notifications"
                    ),
                ),
                ("verified", models.BooleanField(default=False)),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Tell us about yourself",
                        max_length=500,
                        null=True,
                        verbose_name="About Yourself",
                    ),
                ),
                (
                    "header_image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=["middle", "center"],
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[1600, 400],
                        upload_to="headers/",
                    ),
                ),
                (
                    "avatar",
                    django_resized.forms.ResizedImageField(
                        crop=["middle", "center"],
                        default="/defaults/avatar.jpg",
                        force_format=None,
                        keep_meta=True,
                        quality=-1,
                        scale=None,
                        size=[600, 600],
                        upload_to="avatars/",
                        verbose_name="UserProfile Image",
                    ),
                ),
                ("use_gravatar", models.BooleanField(default=False)),
                ("dark_mode", models.BooleanField(default=True)),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True,
                        help_text="It help to know when is your birthday",
                        null=True,
                    ),
                ),
                (
                    "allow_nsfw",
                    models.BooleanField(
                        default=False, verbose_name="Allow NSFW Content"
                    ),
                ),
                ("auth_token", models.CharField(blank=True, max_length=255, null=True)),
                ("badges", models.ManyToManyField(blank=True, to="core.badge")),
                (
                    "follows",
                    models.ManyToManyField(
                        related_name="followed_by", to="account.userprofile"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-25 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vit", "0009_vit_reply_to_alter_vit_image_alter_vit_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vit",
            name="reply_to",
        ),
    ]

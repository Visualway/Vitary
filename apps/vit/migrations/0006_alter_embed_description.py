# Generated by Django 4.0.2 on 2022-06-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit', '0005_remove_embed_embed_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embed',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]

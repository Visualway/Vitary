# Generated by Django 4.0.2 on 2022-11-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_alter_token_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='DevProfile',
            new_name='devProfile',
        ),
    ]

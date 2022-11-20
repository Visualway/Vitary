# Generated by Django 4.0.2 on 2022-11-17 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('developer', '0005_rename_devprofile_token_devprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('private_key', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('payload_url', models.CharField(max_length=50)),
                ('event_type', models.CharField(blank=True, choices=[('on_vit_mention', 'On Vit Mention'), ('on_comment_mention', 'On Comment Mention'), ('on_follow', 'On Follow'), ('on_message', 'On Message')], max_length=50, null=True)),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], default='GET', max_length=5)),
                ('content_type', models.CharField(choices=[('application/json', 'application/json'), ('application/x-www-form-urlencoded', 'application/x-www-form-urlencoded')], default='application/json', max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('required_authentication', models.BooleanField(default=False)),
                ('bot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='developer.bot')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

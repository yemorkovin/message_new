# Generated by Django 5.0.6 on 2024-08-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_chat_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

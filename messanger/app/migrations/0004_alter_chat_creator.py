# Generated by Django 5.0.6 on 2024-07-25 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_chat_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='app.user'),
        ),
    ]

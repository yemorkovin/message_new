# Generated by Django 5.0.6 on 2024-07-25 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_suc_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='suc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontocontact',
            name='phone_number',
            field=models.CharField(default='DNE', max_length=16),
        ),
    ]
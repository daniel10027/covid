# Generated by Django 3.0.5 on 2020-04-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200424_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='localite',
            name='gueri',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0004_sk'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]

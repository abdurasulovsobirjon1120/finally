# Generated by Django 5.0.4 on 2024-05-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_codeconfirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

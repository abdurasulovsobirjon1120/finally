# Generated by Django 5.0.4 on 2024-05-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='tag',
            field=models.CharField(choices=[('worls', 'world'), ('local', 'local'), ('sport', 'sport')], default=-1, max_length=10),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ideas", "0002_ideastar"),
    ]

    operations = [
        migrations.AddField(
            model_name="ideastar",
            name="star",
            field=models.BooleanField(default=False),
        ),
    ]

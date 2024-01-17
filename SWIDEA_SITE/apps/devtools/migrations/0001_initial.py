# Generated by Django 5.0.1 on 2024-01-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Devtool",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=24, verbose_name="이름")),
                ("kind", models.CharField(max_length=255, verbose_name="종류")),
                ("content", models.TextField(verbose_name="개발툴 설명")),
            ],
        ),
    ]

# Generated by Django 4.2.17 on 2025-01-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_chat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

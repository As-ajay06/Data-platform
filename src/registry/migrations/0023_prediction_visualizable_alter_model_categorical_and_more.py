# Generated by Django 4.2.5 on 2023-12-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0022_remove_model_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="visualizable",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="model",
            name="categorical",
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name="model",
            name="spatial",
            field=models.BooleanField(default=None),
        ),
    ]

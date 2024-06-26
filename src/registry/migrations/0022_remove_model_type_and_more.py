# Generated by Django 4.2.5 on 2023-12-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0021_prediction_compatible_predictions_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="model",
            name="type",
        ),
        migrations.RemoveField(
            model_name="prediction",
            name="compatible_predictions",
        ),
        migrations.AddField(
            model_name="model",
            name="categorical",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="model",
            name="spatial",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="prediction",
            name="date_end_prediction",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="prediction",
            name="date_ini_prediction",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="prediction",
            name="metadata",
            field=models.BooleanField(default=False),
        ),
    ]

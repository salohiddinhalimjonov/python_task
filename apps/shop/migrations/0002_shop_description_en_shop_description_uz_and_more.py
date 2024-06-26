# Generated by Django 4.2.11 on 2024-04-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="shop",
            name="description_uz",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_en",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_uz",
            field=models.CharField(max_length=256, null=True),
        ),
    ]

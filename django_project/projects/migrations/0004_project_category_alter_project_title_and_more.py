# Generated by Django 4.2 on 2023-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="category",
            field=models.CharField(
                choices=[
                    ("health", "Health"),
                    ("education", "Education"),
                    ("environment", "Environment"),
                    ("animal", "Animal"),
                    ("culture & art", "Culture & Art"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name="thumbnail",
            name="image_url",
            field=models.CharField(max_length=255),
        ),
    ]
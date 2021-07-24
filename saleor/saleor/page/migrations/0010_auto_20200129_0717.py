# Generated by Django 2.2.9 on 2020-01-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0009_auto_20191108_0402"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="page", name="title", field=models.CharField(max_length=250),
        ),
    ]

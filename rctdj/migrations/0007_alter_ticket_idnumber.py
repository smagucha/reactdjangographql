# Generated by Django 3.2 on 2022-03-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rctdj', '0006_auto_20220311_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='IDNumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
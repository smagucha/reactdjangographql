# Generated by Django 3.2 on 2022-03-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rctdj', '0008_alter_ticket_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

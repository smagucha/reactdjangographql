# Generated by Django 3.2 on 2022-02-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rctdj', '0003_auto_20220222_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='routes',
            options={'verbose_name_plural': 'Routes'},
        ),
        migrations.RenameField(
            model_name='routes',
            old_name='from_to',
            new_name='From',
        ),
        migrations.AddField(
            model_name='routes',
            name='To',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0011_auto_20200426_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='description_large_final',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='description_small_final',
            field=models.TextField(blank=True),
        ),
    ]
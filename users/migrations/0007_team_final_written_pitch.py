# Generated by Django 3.0.3 on 2020-04-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200425_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='final_written_pitch',
            field=models.TextField(blank=True),
        ),
    ]

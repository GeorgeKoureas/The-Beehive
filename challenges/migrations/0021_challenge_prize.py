# Generated by Django 3.0.3 on 2020-05-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0020_auto_20200506_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='prize',
            field=models.CharField(default=1000, max_length=50),
            preserve_default=False,
        ),
    ]

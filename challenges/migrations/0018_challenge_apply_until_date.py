# Generated by Django 3.0.3 on 2020-05-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0017_auto_20200429_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='apply_until_date',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0019_auto_20200505_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='apply_until_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]

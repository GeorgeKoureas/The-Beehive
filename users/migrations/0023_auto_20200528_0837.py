# Generated by Django 3.0.3 on 2020-05-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-27 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200427_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='signs',
        ),
    ]
# Generated by Django 3.0.3 on 2020-04-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_team_member_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='signs',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-27 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_team_signs'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='signs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]

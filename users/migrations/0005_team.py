# Generated by Django 3.0.3 on 2020-04-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0008_auto_20200423_1457'),
        ('users', '0004_auto_20200423_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
                ('members', models.ManyToManyField(blank=True, to='users.Profile')),
            ],
        ),
    ]

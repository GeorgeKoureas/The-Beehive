# Generated by Django 3.0.3 on 2020-05-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0022_auto_20200508_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='cover_image',
            field=models.ImageField(default='default_challenge.jpg', upload_to='challenge_pics'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-10-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profiles/'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_skill_is_key_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='skills'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]

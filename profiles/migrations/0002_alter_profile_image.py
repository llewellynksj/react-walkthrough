# Generated by Django 3.2.22 on 2023-10-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../PP5/default_profile_vfrj2n.jpg', upload_to='images/'),
        ),
    ]
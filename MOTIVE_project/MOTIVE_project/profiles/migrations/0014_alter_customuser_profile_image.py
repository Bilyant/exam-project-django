# Generated by Django 4.2.4 on 2023-08-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_customuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

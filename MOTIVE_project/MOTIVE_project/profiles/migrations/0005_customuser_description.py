# Generated by Django 4.2.4 on 2023-08-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_customuser_first_name_customuser_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default', max_length=40),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-17 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_alter_comments_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-created',), 'verbose_name': 'Comments'},
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_forumratings'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='forumratings',
            unique_together=set(),
        ),
    ]

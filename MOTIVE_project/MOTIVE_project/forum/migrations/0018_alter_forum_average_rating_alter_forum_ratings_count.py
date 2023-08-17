# Generated by Django 4.2.4 on 2023-08-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_forum_main_image_forum_side_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='average_rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='ratings_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
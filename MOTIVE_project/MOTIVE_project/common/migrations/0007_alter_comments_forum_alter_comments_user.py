# Generated by Django 4.2.4 on 2023-08-09 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_forum_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0006_comments_updated_alter_comments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='forum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.forum'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

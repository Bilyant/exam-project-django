# Generated by Django 4.2.4 on 2023-08-05 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_forum_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.topics'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200327_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='user',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'girl'), (1, 'boy')], null=True),
        ),
    ]

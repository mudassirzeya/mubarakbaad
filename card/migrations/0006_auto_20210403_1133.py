# Generated by Django 3.1.5 on 2021-04-03 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_auto_20210403_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_card',
            name='english',
        ),
        migrations.RemoveField(
            model_name='create_card',
            name='urdu',
        ),
    ]

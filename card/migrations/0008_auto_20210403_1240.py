# Generated by Django 3.1.5 on 2021-04-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_create_card_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_card',
            name='languages',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_savedgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedgame',
            name='match',
            field=models.CharField(max_length=80),
        ),
    ]

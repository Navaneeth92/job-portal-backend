# Generated by Django 3.2 on 2021-11-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=48, unique=True, verbose_name='name'),
        ),
    ]

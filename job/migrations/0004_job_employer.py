# Generated by Django 3.2 on 2021-11-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211124_1103'),
        ('job', '0003_alter_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='accounts.employer', verbose_name='employer'),
            preserve_default=False,
        ),
    ]

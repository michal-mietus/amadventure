# Generated by Django 2.1.5 on 2019-03-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero_upgrade_system', '0011_statistic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='hero',
        ),
        migrations.DeleteModel(
            name='Statistic',
        ),
    ]

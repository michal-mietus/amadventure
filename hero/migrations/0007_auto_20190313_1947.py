# Generated by Django 2.1.5 on 2019-03-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_auto_20190311_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='ability_points',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='statistic_points',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]

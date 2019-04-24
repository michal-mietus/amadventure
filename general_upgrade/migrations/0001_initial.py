# Generated by Django 2.1.7 on 2019-04-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('strength', 'strength'), ('agility', 'agility'), ('intelligence', 'intelligence'), ('', '')], max_length=35)),
                ('points', models.PositiveIntegerField(default=5)),
            ],
        ),
    ]

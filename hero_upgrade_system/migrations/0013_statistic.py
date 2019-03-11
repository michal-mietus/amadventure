# Generated by Django 2.1.5 on 2019-03-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_auto_20190311_1721'),
        ('hero_upgrade_system', '0012_auto_20190311_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('strength', 'strength'), ('agility', 'agility'), ('intelligence', 'intelligence')], max_length=35)),
                ('points', models.PositiveIntegerField()),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Hero')),
            ],
        ),
    ]

# Generated by Django 2.1.5 on 2019-03-09 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero_upgrade_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('unblock_level', models.PositiveIntegerField()),
                ('level', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('passive', 'passive'), ('active', 'active')], max_length=35)),
                ('ability_module', models.CharField(max_length=100)),
                ('ability_function', models.CharField(max_length=100)),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_upgrade_system.Occupation')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_upgrade_system.Ability')),
            ],
        ),
    ]
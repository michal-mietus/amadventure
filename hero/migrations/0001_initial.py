# Generated by Django 2.1.7 on 2019-03-29 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('unblock_level', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('passive', 'passive'), ('active', 'active')], max_length=35)),
                ('function', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('statistic_points', models.PositiveIntegerField(default=15)),
                ('ability_points', models.PositiveIntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='HeroAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=0)),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Ability')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Hero')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.HeroAbility')),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('warrior', 'Warrior'), ('thief', 'Thief'), ('mage', 'Mage')], max_length=35)),
                ('module', models.CharField(choices=[('hero.models.occupations.warrior', 'hero.models.occupations.warrior'), ('hero.models.occupations.mage', 'hero.models.occupations.mage'), ('hero.models.occupations.thief', 'hero.models.occupations.thief')], max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('strength', 'strength'), ('agility', 'agility'), ('intelligence', 'intelligence')], max_length=35)),
                ('points', models.PositiveIntegerField(default=5)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Hero')),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Occupation'),
        ),
        migrations.AddField(
            model_name='hero',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ability',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Occupation'),
        ),
        migrations.AddField(
            model_name='ability',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.Ability'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-26 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_upgrade', '0001_initial'),
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('rarity', models.CharField(choices=[('common', 'common'), ('rare', 'rare'), ('legendary', 'legendary')], max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStatistic',
            fields=[
                ('statistic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='general_upgrade.Statistic')),
            ],
            bases=('general_upgrade.statistic',),
        ),
        migrations.CreateModel(
            name='ItemWithStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[(1, 'easy'), (1.5, 'medium'), (2, 'hard')], max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.Location')),
            ],
        ),
        migrations.CreateModel(
            name='MobClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_statistic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HeroItem',
            fields=[
                ('itemwithstatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='artifical.ItemWithStatistics')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.Hero')),
            ],
            bases=('artifical.itemwithstatistics',),
        ),
        migrations.AddField(
            model_name='mob',
            name='mob_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.MobClass'),
        ),
        migrations.AddField(
            model_name='itemwithstatistics',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.ItemGeneral'),
        ),
        migrations.AddField(
            model_name='itemstatistic',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.ItemWithStatistics'),
        ),
    ]

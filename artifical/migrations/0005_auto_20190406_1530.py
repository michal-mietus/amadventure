# Generated by Django 2.1.7 on 2019-04-06 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_upgrade', '0003_auto_20190405_1624'),
        ('artifical', '0004_auto_20190406_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='FightingMob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FightingMobStatistics',
            fields=[
                ('statistic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='general_upgrade.Statistic')),
                ('mob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.FightingMob')),
            ],
            bases=('general_upgrade.statistic',),
        ),
        migrations.RemoveField(
            model_name='mobstatistics',
            name='mob',
        ),
        migrations.RemoveField(
            model_name='mobstatistics',
            name='statistic_ptr',
        ),
        migrations.RemoveField(
            model_name='mob',
            name='level',
        ),
        migrations.DeleteModel(
            name='MobStatistics',
        ),
        migrations.AddField(
            model_name='fightingmob',
            name='mob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.Mob'),
        ),
    ]

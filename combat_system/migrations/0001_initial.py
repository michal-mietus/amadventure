# Generated by Django 2.1.7 on 2019-04-29 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_upgrade', '0001_initial'),
        ('artifical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FightingMob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=1)),
                ('mob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artifical.Mob')),
            ],
        ),
        migrations.CreateModel(
            name='FightingMobStatistic',
            fields=[
                ('statistic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='general_upgrade.Statistic')),
                ('mob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combat_system.FightingMob')),
            ],
            bases=('general_upgrade.statistic',),
        ),
    ]

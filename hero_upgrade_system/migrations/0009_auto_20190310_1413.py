# Generated by Django 2.1.5 on 2019-03-10 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero_upgrade_system', '0008_auto_20190310_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='ability',
            name='level',
        ),
        migrations.AddField(
            model_name='heroability',
            name='ability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_upgrade_system.Ability'),
        ),
        migrations.AddField(
            model_name='heroability',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero_upgrade_system.HeroAbility'),
        ),
    ]
# Generated by Django 2.1.5 on 2019-03-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_upgrade_system', '0002_ability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ability',
            old_name='parent',
            new_name='parent_ability',
        ),
        migrations.RemoveField(
            model_name='ability',
            name='ability_module',
        ),
        migrations.AddField(
            model_name='occupation',
            name='module',
            field=models.CharField(choices=[('warrior', 'hero_upgrade_system.models.abilities.warrior'), ('mage', 'hero_upgrade_system.models.abilities.mage'), ('thief', 'hero_upgrade_system.models.abilities.thief')], default='hero_upgrade_system.models.abilities.warrior', max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-03-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_upgrade_system', '0003_auto_20190309_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='name',
            field=models.CharField(choices=[('warrior', 'Warrior'), ('thief', 'Thief'), ('mage', 'Mage')], max_length=35),
        ),
    ]

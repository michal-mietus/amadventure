# Generated by Django 2.1.7 on 2019-04-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifical', '0006_auto_20190406_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobclass',
            name='name',
            field=models.CharField(choices=[('physic', 'strength'), ('magic', 'intelligence'), ('agile', 'agility'), ('tanky', 'health')], max_length=50),
        ),
    ]
# Generated by Django 2.1.7 on 2019-04-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_upgrade', '0002_auto_20190405_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='name',
            field=models.CharField(choices=[('strength', 'strength'), ('agility', 'agility'), ('intelligence', 'intelligence'), ('health', 'health')], max_length=35),
        ),
    ]

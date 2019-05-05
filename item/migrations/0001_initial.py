# Generated by Django 2.1.7 on 2019-05-02 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_upgrade', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('rarity', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='assets/items')),
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
            name='TemporaryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemstatistic',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.TemporaryItem'),
        ),
    ]

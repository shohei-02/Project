# Generated by Django 2.1.3 on 2018-12-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbrecord', '0002_playerstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='inning_score',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='playerstats',
            name='daseki',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerstats',
            name='dasuu',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

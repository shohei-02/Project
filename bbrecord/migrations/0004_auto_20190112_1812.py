# Generated by Django 2.1.3 on 2019-01-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbrecord', '0003_auto_20181215_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='inning_score',
            new_name='my_inning_score',
        ),
        migrations.AddField(
            model_name='game',
            name='opponent_inning_score',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
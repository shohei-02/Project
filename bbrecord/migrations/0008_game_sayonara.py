# Generated by Django 2.1.3 on 2019-01-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbrecord', '0007_auto_20190127_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='sayonara',
            field=models.BooleanField(default=False),
        ),
    ]

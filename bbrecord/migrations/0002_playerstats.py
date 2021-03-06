# Generated by Django 2.1.3 on 2018-12-05 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbrecord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playerstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.IntegerField(blank=True, null=True)),
                ('Walk', models.IntegerField(blank=True, null=True)),
                ('stlike_out', models.IntegerField(blank=True, null=True)),
                ('position', models.CharField(blank=True, max_length=10, null=True)),
                ('dajun', models.IntegerField(blank=True, null=True)),
                ('starting_member', models.BooleanField(default=False)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbrecord.Game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbrecord.User')),
            ],
        ),
    ]

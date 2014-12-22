# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_fight', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
                ('full_name', models.CharField(max_length=120)),
                ('number_of_tweets', models.PositiveIntegerField()),
                ('number_of_followers', models.PositiveIntegerField()),
                ('number_of_friends', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fight',
            name='user1',
            field=models.ForeignKey(related_name='oponent1', to='fight.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fight',
            name='user2',
            field=models.ForeignKey(related_name='oponent2', to='fight.User'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_name', models.CharField(max_length=100)),
                ('collection_user', models.CharField(max_length=50)),
                ('collection_pass', models.CharField(max_length=50)),
                ('host_name', models.CharField(max_length=50)),
                ('port_number', models.IntegerField()),
                ('database_name', models.CharField(max_length=100)),
                ('authsource_database', models.CharField(max_length=100)),
                ('collection_description', models.CharField(max_length=600)),
                ('collection_uri', models.CharField(max_length=600, null=True, blank=True)),
                ('collection_rowcount', models.IntegerField(null=True, blank=True)),
                ('collection_querylink', models.CharField(max_length=1, null=True, blank=True)),
                ('collection_querylimit', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_text', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1, choices=[(b'N', b'New'), (b'R', b'Running'), (b'C', b'Completed'), (b'S', b'Success'), (b'F', b'Failed')])),
                ('collection', models.ForeignKey(to='mongoquery.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tardis_user', models.CharField(max_length=50)),
                ('collection', models.ManyToManyField(to='mongoquery.Collection')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelcompletion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cell',
            name='channels',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='username',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='patch_clamp',
        ),
        migrations.RemoveField(
            model_name='graphdata',
            name='graph',
        ),
        migrations.RemoveField(
            model_name='ionchannelmodel',
            name='channel_name',
        ),
        migrations.RemoveField(
            model_name='ionchannelmodel',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='ionchannelmodel',
            name='graph',
        ),
        migrations.RemoveField(
            model_name='ionchannelmodel',
            name='references',
        ),
        migrations.RemoveField(
            model_name='ionchannelmodel',
            name='username',
        ),
        migrations.RemoveField(
            model_name='patchclamp',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='channels',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='username',
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
        migrations.DeleteModel(
            name='GraphData',
        ),
        migrations.DeleteModel(
            name='IonChannel',
        ),
        migrations.DeleteModel(
            name='IonChannelModel',
        ),
        migrations.DeleteModel(
            name='PatchClamp',
        ),
        migrations.DeleteModel(
            name='Reference',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influential_figure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='influentialfigure',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influentialfigure',
            name='nationality',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

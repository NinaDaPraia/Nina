# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influential_figures', '0003_auto_20150629_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmovement',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]

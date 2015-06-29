# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influential_figure', '0002_auto_20150528_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMovement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='influentialfigure',
            old_name='nationality',
            new_name='description',
        ),
        migrations.AddField(
            model_name='influentialfigure',
            name='image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influentialfigure',
            name='social_movements',
            field=models.ManyToManyField(to='influential_figure.SocialMovement'),
        ),
    ]

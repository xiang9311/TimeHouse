# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useroption',
            name='word',
            field=models.CharField(max_length=2000, default=''),
            preserve_default=False,
        ),
    ]

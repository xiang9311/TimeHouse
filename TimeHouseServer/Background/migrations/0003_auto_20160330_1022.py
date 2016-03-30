# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Background', '0002_auto_20160329_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='article_title',
            field=models.CharField(max_length=300, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collect',
            name='article_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collect',
            name='organization_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

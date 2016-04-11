# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOption',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('choise', models.BooleanField()),
                ('choose_time', models.DateTimeField()),
            ],
        ),
    ]

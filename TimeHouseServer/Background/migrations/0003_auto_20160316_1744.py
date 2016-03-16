# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Background', '0002_auto_20160316_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleculture',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articleforeign',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlehistory',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlehuman',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlejoke',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articleliterature',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlenews',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlephilosophy',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='articlephoto',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='textandimage',
            old_name='organization_id',
            new_name='organization',
        ),
    ]

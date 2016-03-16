# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Background', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('pw_md5', models.CharField(max_length=70)),
                ('wx_no', models.CharField(max_length=100)),
                ('wb_no', models.CharField(max_length=100)),
                ('is_trusteeship', models.BooleanField()),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('pw_md5', models.CharField(max_length=70)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='articleculture',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articleforeign',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlehistory',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlehuman',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlejoke',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articleliterature',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlephilosophy',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='articlephoto',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='textandimage',
            name='user_id',
        ),
        migrations.AddField(
            model_name='articleculture',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleforeign',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlehistory',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlehuman',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlejoke',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleliterature',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlenews',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlephilosophy',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlephoto',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textandimage',
            name='organization_id',
            field=models.ForeignKey(default='', to='Background.Organization'),
            preserve_default=False,
        ),
    ]

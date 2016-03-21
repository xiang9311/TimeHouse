# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Background', '0004_auto_20160321_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDeep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=100)),
                ('content_type', models.IntegerField()),
                ('article_type', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('sub_content', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('cover_url', models.CharField(max_length=100)),
                ('content_url', models.CharField(max_length=200)),
                ('read_count', models.IntegerField()),
                ('collect_count', models.IntegerField()),
                ('share_count', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('organization', models.ForeignKey(to='Background.Organization')),
            ],
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='organization',
        ),
        migrations.DeleteModel(
            name='ArticleNews',
        ),
    ]

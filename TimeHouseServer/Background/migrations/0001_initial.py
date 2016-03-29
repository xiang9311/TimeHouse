# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDeep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleForeign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleHuman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleJoke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('article_id', models.IntegerField()),
                ('collect_type', models.IntegerField()),
                ('collect_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('pw_md5', models.CharField(max_length=70)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TextAndImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('articleId', models.IntegerField()),
                ('text', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(to='Background.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('pw_md5', models.CharField(max_length=70)),
                ('wx_no', models.CharField(max_length=100)),
                ('wb_no', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='collect',
            name='user_id',
            field=models.ForeignKey(to='Background.User'),
        ),
        migrations.AddField(
            model_name='articlephoto',
            name='organization',
            field=models.ForeignKey(to='Background.Organization'),
        ),
        migrations.AddField(
            model_name='articlejoke',
            name='organization',
            field=models.ForeignKey(to='Background.Organization'),
        ),
        migrations.AddField(
            model_name='articlehuman',
            name='organization',
            field=models.ForeignKey(to='Background.Organization'),
        ),
        migrations.AddField(
            model_name='articleforeign',
            name='organization',
            field=models.ForeignKey(to='Background.Organization'),
        ),
        migrations.AddField(
            model_name='articledeep',
            name='organization',
            field=models.ForeignKey(to='Background.Organization'),
        ),
    ]

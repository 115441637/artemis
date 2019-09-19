# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-17 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=32, unique=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=100, verbose_name='\u5bc6\u7801')),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='\u90ae\u7bb1')),
                ('tel', models.CharField(max_length=20, verbose_name='\u624b\u673a\u53f7')),
                ('create_date', models.DateField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.IntegerField(verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\x96\xb9id')),
                ('dept_id', models.IntegerField(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8id')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 't_ops_notification',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('url', models.CharField(max_length=128, verbose_name=b'\xe8\xb7\xaf\xe7\x94\xb1')),
                ('action', models.CharField(default=b'', max_length=32, verbose_name=b'\xe5\x8a\xa8\xe4\xbd\x9c')),
            ],
            options={
                'verbose_name': '\u6743\u9650',
                'verbose_name_plural': '\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u7ec4',
                'verbose_name_plural': '\u6743\u9650\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('detail', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='\u90ae\u7bb1')),
                ('desc', models.CharField(blank=True, max_length=64, null=True)),
                ('permission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authority.Permission')),
            ],
            options={
                'verbose_name': '\u89d2\u8272',
                'verbose_name_plural': '\u89d2\u8272',
            },
        ),
        migrations.AddField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authority.PermissionGroup'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authority.Role', verbose_name='\u90e8\u95e8'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-04 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200703_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=datetime.datetime(2020, 7, 4, 15, 38, 14, 822437, tzinfo=utc), max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=250, verbose_name='auth.User'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=250, verbose_name='auth.User'),
        ),
    ]

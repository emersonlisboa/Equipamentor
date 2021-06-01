# Generated by Django 3.2 on 2021-06-01 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20210601_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='planDate',
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 20, 24, 18, 48202, tzinfo=utc)),
        ),
    ]

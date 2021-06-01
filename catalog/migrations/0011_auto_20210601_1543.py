# Generated by Django 3.2 on 2021-06-01 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20210601_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeer',
            name='admissionDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='executedDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='planDate',
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 19, 43, 24, 515901, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-05 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0009_auto_20200505_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='buydate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 21, 2, 31, 916989)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 21, 2, 31, 915499)),
        ),
    ]
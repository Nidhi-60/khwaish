# Generated by Django 3.0.5 on 2020-05-04 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0009_auto_20200504_1149'),
        ('Orders', '0002_auto_20200504_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='buydate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 11, 49, 56, 377609)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 11, 49, 56, 376157)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artistpainting'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-10 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0027_auto_20200510_1350'),
        ('Blogs', '0005_auto_20200510_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='artist',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Artists.Artistpainting'),
        ),
        migrations.AddField(
            model_name='review',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Artists.Paintingofcategory'),
        ),
        migrations.AlterField(
            model_name='artistblog',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artist'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 13, 50, 22, 503840)),
        ),
    ]

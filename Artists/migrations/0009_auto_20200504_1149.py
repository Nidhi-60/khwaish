# Generated by Django 3.0.5 on 2020-05-04 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0008_auto_20200504_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistpainting',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artist'),
        ),
    ]

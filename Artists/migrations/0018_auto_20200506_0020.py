# Generated by Django 3.0.5 on 2020-05-05 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0017_auto_20200505_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistpainting',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artist'),
        ),
    ]

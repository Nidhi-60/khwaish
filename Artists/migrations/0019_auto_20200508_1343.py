# Generated by Django 3.0.5 on 2020-05-08 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0018_auto_20200506_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistpainting',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artist'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-04 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0007_auto_20200503_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistpainting',
            name='paintingcode',
            field=models.CharField(default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='paintingofcategory',
            name='paintingcode',
            field=models.CharField(default='C', max_length=2),
        ),
        migrations.AlterField(
            model_name='artistpainting',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artists.Artist'),
        ),
    ]
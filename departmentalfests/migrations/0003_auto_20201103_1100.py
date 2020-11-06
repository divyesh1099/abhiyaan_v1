# Generated by Django 3.1.2 on 2020-11-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentalfests', '0002_auto_20201102_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='department',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='department',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='departmentalfest',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='departmentalfest',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='departmentalfest',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='departmentalfest',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
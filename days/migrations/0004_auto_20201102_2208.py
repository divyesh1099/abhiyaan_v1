# Generated by Django 3.1.2 on 2020-11-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0003_auto_20201101_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='days',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='rules',
            field=models.TextField(blank=True),
        ),
    ]

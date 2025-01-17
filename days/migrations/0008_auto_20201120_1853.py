# Generated by Django 3.1.2 on 2020-11-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0007_auto_20201103_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='trialimage',
        ),
        migrations.AddField(
            model_name='event',
            name='registrationform',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='day',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='day',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='day',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='days',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='days',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='days',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventhead',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]

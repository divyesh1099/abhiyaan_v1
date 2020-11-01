# Generated by Django 3.1.2 on 2020-10-31 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('dayImageOne', models.CharField(max_length=1000)),
                ('dayImageTwo', models.CharField(max_length=1000)),
                ('dayImageThree', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('eventhead', models.CharField(max_length=64)),
                ('rules', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daysImageOne', models.CharField(max_length=1000)),
                ('daysImageTwo', models.CharField(max_length=1000)),
                ('daysImageThree', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayofdays', to='days.day')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventsofday', to='days.events'),
        ),
    ]

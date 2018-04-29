# Generated by Django 2.0.4 on 2018-04-29 11:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180429_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('real_address', models.CharField(max_length=30)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Пункт выдачи',
                'verbose_name_plural': 'Пункты выдачи',
            },
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('C', 'Canceled'), ('I', 'Incomplete'), ('S', 'Completed'), ('R', 'Rejected')], default='I', max_length=3),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Point'),
        ),
    ]

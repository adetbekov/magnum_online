# Generated by Django 2.0.4 on 2018-05-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180429_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('C', 'Canceled'), ('I', 'Incomplete'), ('R', 'Rejected'), ('S', 'Completed')], default='I', max_length=3),
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180531_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('I', 'Incomplete'), ('S', 'Completed'), ('R', 'Rejected'), ('C', 'Canceled')], default='I', max_length=3),
        ),
    ]
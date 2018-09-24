# Generated by Django 2.1.1 on 2018-09-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0004_auto_20180918_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='Date of event'),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
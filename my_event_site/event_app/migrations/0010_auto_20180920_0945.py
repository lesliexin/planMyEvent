# Generated by Django 2.1.1 on 2018-09-20 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0009_auto_20180920_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='a_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.Guestlist'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-25 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20200425_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='correctanswer',
        ),
        migrations.AddField(
            model_name='game',
            name='correctCart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='car.Car'),
        ),
    ]
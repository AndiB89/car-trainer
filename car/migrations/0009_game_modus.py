# Generated by Django 3.0.5 on 2020-04-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20200425_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='modus',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

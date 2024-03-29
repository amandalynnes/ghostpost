# Generated by Django 3.1.6 on 2021-02-18 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2021, 2, 18, 14, 51, 40, 66266, tzinfo=utc))),
                ('choose', models.CharField(choices=[('1', 'toast'), ('2', 'roast')], max_length=1)),
            ],
        ),
    ]

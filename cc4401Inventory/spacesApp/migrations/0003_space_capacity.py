# Generated by Django 2.0.4 on 2018-08-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacesApp', '0002_auto_20180801_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='capacity',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.8 on 2021-07-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210726_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'StandardPost'), (1, 'BlankPage')], default=0),
        ),
    ]

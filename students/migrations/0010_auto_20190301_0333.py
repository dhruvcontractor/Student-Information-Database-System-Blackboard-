# Generated by Django 2.1.4 on 2019-03-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20190301_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Faculty')], default=1),
        ),
    ]

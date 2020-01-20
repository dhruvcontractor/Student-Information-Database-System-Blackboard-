# Generated by Django 2.1.4 on 2019-03-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='banner_id',
            field=models.TextField(default=' ', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='total_credit',
            field=models.TextField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
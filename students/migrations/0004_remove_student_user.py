# Generated by Django 2.1.4 on 2019-02-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
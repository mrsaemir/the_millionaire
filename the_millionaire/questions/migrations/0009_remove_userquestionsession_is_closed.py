# Generated by Django 3.1.13 on 2021-09-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20210906_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquestionsession',
            name='is_closed',
        ),
    ]

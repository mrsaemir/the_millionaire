# Generated by Django 3.1.13 on 2021-09-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20210906_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestionsession',
            name='answers',
            field=models.JSONField(default=dict),
        ),
    ]
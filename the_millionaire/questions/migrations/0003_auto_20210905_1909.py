# Generated by Django 3.1.13 on 2021-09-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20210905_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_answer', to='questions.questionoption'),
        ),
    ]

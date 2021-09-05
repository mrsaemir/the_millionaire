# Generated by Django 3.1.13 on 2021-09-05 18:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('score', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(20)])),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.JSONField()),
                ('score', models.PositiveIntegerField(default=0)),
                ('questions', models.ManyToManyField(to='questions.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questions.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='question_answer', to='questions.questionoption'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(check=models.Q(('score__gte', 5), ('score__lte', 20)), name='Score value should be between 5 and 20.'),
        ),
    ]

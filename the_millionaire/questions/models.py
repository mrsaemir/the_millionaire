from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .managers import QuestionManager
from typing import Union, Tuple

User = get_user_model()


class Question(models.Model):
    """
    Question model and it's corresponding score.
    A question may multiple options, but it only has one answer.
    """

    title = models.CharField(max_length=200)
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(20)
        ]
    )
    answer = models.ForeignKey(
        'QuestionOption', null=True, blank=True, related_name='question_answer', on_delete=models.SET_NULL
    )

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.answer and self.answer.question != self:
            raise ValidationError(
                _("Answer of a question should be one of it's options.")
            )

        if not self.answer and self.user_questions.exists(): # noqa
            raise ValidationError(
                _("Can't unset answer because this question is being used by some users.")
            )

        return super(Question, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(score__gte=5) & models.Q(score__lte=20),
                name=_("Score value should be between 5 and 20.")
            ),
        ]


class QuestionOption(models.Model):
    """
    Options related to a question.
    """

    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.text


class UserQuestionSession(models.Model):
    """
    A model that connects a user to some questions
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='user_questions')
    answers = models.JSONField(default=list)
    score = models.PositiveIntegerField(default=0)

    # an indicator that shows if a question session is closed.
    # when a session is closed, the user will not be able to submit any answers
    # or to do any other change.
    is_closed = models.BooleanField(default=False)

    def has_answered(self, question):
        """
        Checking if a user has answered a specific question.
        """

        for answer in self.answers:
            if answer['question_id'] == question.id:
                return True
        return False

    def set_answer(self, question, answer) -> Union[None, Tuple[bool, QuestionOption]]:
        """
        Sets user answer for a specific question.
        this function will either return None or a tuple.

        returning None means that the user answer is not submitted either because it is invalid or the
        user has answer it before.

        returning a tuple means that the answer is submitted.
        the first element of the tuple is a boolean that shows if the submitted answer is the answer to the question.

        the second element is always the answer of the question.
        """
        if self.has_answered(question):
            # returns none meaning that the answer is not submitted.
            return None

        if answer not in question.options.all():
            # the answer is not an option of the question
            return None

        self.answers.append({
            "question_id": question.id,
            "answer_id": answer.id
        })

        is_answered_correct = question.answer == answer
        if is_answered_correct:
            self.score += question.score

        self.save()

        return is_answered_correct, question.answer


from django.conf import settings
from .models import Question, UserQuestionSession


def create_question_session(user, number_of_question=settings.NUMBER_OF_QUESTIONS):
    questions = Question.objects.published().order_by('?')[:number_of_question]
    session = UserQuestionSession(
        user=user
    )
    session.save()
    session.questions.add(*questions)
    return session


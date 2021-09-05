from django.db import models


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super(QuestionManager, self).get_queryset().select_related(
            'answer'
        )


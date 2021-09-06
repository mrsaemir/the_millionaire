from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserQuestionSession
from .utils import create_question_session

from .serializers import (
    UserQuestionSessionDetailSerializer,
    UserQuestionSessionListSerializer,
    QuestionOptionSerializer,
    SetAnswerSerializer
)


class UserQuestionSessionsView(
    ModelViewSet
):

    permission_classes = (
        IsAuthenticated,
    )

    serializer_class = UserQuestionSessionListSerializer

    def get_queryset(self):
        return UserQuestionSession.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        session = create_question_session(user=request.user)
        return Response(
            UserQuestionSessionDetailSerializer(session, context={'sessions': session}).data,
        )

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response(
            UserQuestionSessionDetailSerializer(obj, context={'session': obj}).data
        )

    @action(detail=True, methods=['post'], url_path='set-answer')
    def set_answer(self, request, pk=None):
        obj = self.get_object()
        serializer = SetAnswerSerializer(data=request.data, context={'session': obj})
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        if not result:
            return Response({"error": _("Failed to submit your answer.")})

        return Response(
            {
                "session": UserQuestionSessionDetailSerializer(obj).data,
                "answer": {
                    "status": result[0],
                    "answer": QuestionOptionSerializer(result[1]).data
                }
            }
        )

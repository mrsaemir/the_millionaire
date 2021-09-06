from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserQuestionSession
from .utils import create_question_session
from .serializers import UserQuestionSessionSerializer


class CreateUserQuestionSessionView(
    CreateAPIView
):

    permission_classes = (
        IsAuthenticated,
    )

    def create(self, request, *args, **kwargs):
        if UserQuestionSession.objects.filter(user=request.user).exists():
            return Response(
                {
                    "error": _("Another user question session is in progress."),
                },
                status=status.HTTP_403_FORBIDDEN
            )

        session = create_question_session(user=request.user)
        return Response(UserQuestionSessionSerializer(session).data, status=status.HTTP_200_OK)


class ListUserQuestionSessionsView(
    ListAPIView
):

    permission_classes = (
        IsAuthenticated,
    )

    def list(self, request, *args, **kwargs):
        sessions = UserQuestionSession.objects.filter(user=request.user)

        return Response(
            UserQuestionSessionSerializer(sessions, many=True).data
        )

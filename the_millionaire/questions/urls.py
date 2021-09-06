from django.urls import path
from .views import CreateUserQuestionSessionView, ListUserQuestionSessionsView


urlpatterns = [
    path('', ListUserQuestionSessionsView.as_view(), name='list-user-question-sessions'),
    path('new-session', CreateUserQuestionSessionView.as_view(), name='create-user-question-session'),
]

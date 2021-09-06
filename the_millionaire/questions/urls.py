
from .views import UserQuestionSessionsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'session', UserQuestionSessionsView, basename='question-session'
)

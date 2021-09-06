
from .views import UserQuestionSessionsView, TopUsers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'session', UserQuestionSessionsView, basename='question-session',
)

router.register(
    'top-users', TopUsers, basename='top-users'
)

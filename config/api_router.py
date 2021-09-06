from django.urls import path, include
from questions.urls import router as questions_router
from users.urls import router as users_router


app_name = "api"
urlpatterns = [
    path('questions/', include(questions_router.urls)),
    path('users/', include(users_router.urls))
]

from django.urls import path, include
from questions.urls import router as questions_router


app_name = "api"
urlpatterns = [
    path('questions/', include(questions_router.urls))
]

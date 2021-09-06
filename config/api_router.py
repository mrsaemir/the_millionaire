from django.urls import path, include
from questions.urls import urlpatterns as question_urls


app_name = "api"
urlpatterns = [
    path('questions/', include(question_urls))
]

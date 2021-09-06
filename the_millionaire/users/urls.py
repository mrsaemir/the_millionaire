from django.urls import path
from rest_framework.routers import DefaultRouter

from the_millionaire.users.api.views import UserViewSet
from the_millionaire.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)


router = DefaultRouter()
router.register("users", UserViewSet)


app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]

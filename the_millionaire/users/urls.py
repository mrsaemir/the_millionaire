from rest_framework.routers import DefaultRouter
from the_millionaire.users.api.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)




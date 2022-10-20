
from .views import RegisterView, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"users", UserViewSet, basename="user-api")
router.register(r"register", RegisterView, basename="register-api")

user_app_routes = router.urls

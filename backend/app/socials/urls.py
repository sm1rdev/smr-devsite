from rest_framework.routers import DefaultRouter
from .views import SocialViewSet


router = DefaultRouter()
router.register(r'', SocialViewSet, basename="social")

urlpatterns = router.urls

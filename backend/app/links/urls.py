from rest_framework.routers import DefaultRouter
from .views import LinkViewSet


router = DefaultRouter()
router.register(r'', LinkViewSet, basename="link")

urlpatterns = router.urls

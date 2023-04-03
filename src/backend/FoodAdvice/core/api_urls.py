from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet, RestaurantViewSet

router = DefaultRouter()
router.register('client', ClientViewSet, basename='client')
router.register('resto', RestaurantViewSet, basename='resto')

urlpatterns = router.urls
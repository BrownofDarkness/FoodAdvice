from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet, RestaurantViewSet, LoginViewSet, CarteViewSet, PlateViewSet

router = DefaultRouter()
router.register('client', ClientViewSet, basename='client')
router.register('resto', RestaurantViewSet, basename='resto')
router.register('login', LoginViewSet, basename='login')
router.register('carte', CarteViewSet, basename='carte')
router.register('plates', PlateViewSet, basename='plates')

urlpatterns = router.urls
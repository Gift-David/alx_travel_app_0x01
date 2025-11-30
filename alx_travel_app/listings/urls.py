from django.urls import path, include
from .views import ListingViewSets, BookingViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booking', BookingViewSets, basename='booking')
router.register(r'listing', ListingViewSets, basename='listing')

urlpatterns = [
    path('', include(router.urls)),
]

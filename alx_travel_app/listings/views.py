from rest_framework import viewsets
from .serializers import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSets(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

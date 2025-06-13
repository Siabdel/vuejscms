
from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

class LandingPageAPIView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

from django.urls import path
from .api_views import LandingPageAPIView

urlpatterns = [
    path('api/landing/<slug:slug>/', LandingPageAPIView.as_view(), name='landing-page-api'),
]

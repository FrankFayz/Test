from django.urls import path
from ads.views import ad_list, health

urlpatterns = [
    path("api/ads/", ad_list, name="ad-list"),
    path("api/health/", health, name="health"),
]

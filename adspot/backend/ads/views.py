import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Advertisement

@require_GET
def ad_list(request):
    ads = Advertisement.objects.filter(is_active=True)
    data = [
        {
            "id": ad.id,
            "title": ad.title,
            "business_name": ad.business_name,
            "description": ad.description,
            "image_url": ad.image_url,
            "link_url": ad.link_url,
            "category": ad.category,
        }
        for ad in ads
    ]
    return JsonResponse(data, safe=False)

@require_GET
def health(request):
    return JsonResponse({"status": "ok", "application": "AdSpot API"})

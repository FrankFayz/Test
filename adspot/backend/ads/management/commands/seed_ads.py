from django.core.management.base import BaseCommand
from ads.models import Advertisement

SAMPLE_ADS = [
    {
        "title": "Upgrade Your Everyday",
        "business_name": "Nova Tech",
        "description": "Discover smart accessories and useful technology for work, study and play.",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1200&q=85",
        "link_url": "https://example.com",
        "category": "Technology",
    },
    {
        "title": "Good Food, Good Mood",
        "business_name": "The Fresh Table",
        "description": "Make your next break delicious with fresh flavours and friendly service.",
        "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1200&q=85",
        "link_url": "https://example.com",
        "category": "Food & Dining",
    },
    {
        "title": "Find Your Own Style",
        "business_name": "Everyday Wear",
        "description": "Explore simple, comfortable looks made for your everyday adventures.",
        "image_url": "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=1200&q=85",
        "link_url": "https://example.com",
        "category": "Fashion",
    },
]

class Command(BaseCommand):
    help = "Insert sample advertisements if the database is empty."

    def handle(self, *args, **options):
        if Advertisement.objects.exists():
            self.stdout.write("Advertisements already exist; skipping sample data.")
            return
        for item in SAMPLE_ADS:
            Advertisement.objects.create(**item)
        self.stdout.write(self.style.SUCCESS("Added 3 sample advertisements."))

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advertisement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("business_name", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("image_url", models.URLField()),
                ("link_url", models.URLField(blank=True)),
                ("category", models.CharField(default="General", max_length=60)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at", "title"]},
        ),
    ]
